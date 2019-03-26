from flask import Flask, render_template, request
from flask import redirect, url_for, jsonify, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from movie_database import Movie, Store, Director, User
from flask import session as login_session
import random
import string
import json

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secret.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Director movie item-catalog"
engine = create_engine(
    'sqlite:///movie_database.db', connect_args={'check_same_thread': False},
    echo=True)
Store.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# For User login
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in range(32))
    login_session['state'] = state
    # return "The current state is %s" %login_session['state']
    director = session.query(Director).all()
    movie = session.query(Movie).all()
    return render_template('login.html', STATE=state, director=director,
                           movie=movie)




# If User already logged
@app.route('/gconnect', methods=['POST'])
def gconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid State parameter'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    code = request.data

    try:
        oauth_flow = flow_from_clientsecrets('client_secret.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])

    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response


    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(
                                 json.dumps(
                                            'Current user already connected'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['email'] = data['email']

    user_id = getUserID(login_session['email'])
    if not user_id:
         user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<center><h2><font color="green">Welcome '
    output += login_session['username']
    output += '!</font></h2></center>'
    output += '<center><img src="'
    output += ' " style = "width: 200px; -webkit-border-radius: 200px;" '
    output += ' " style = "height: 200px;border-radius: 200px;" '
    output += ' " style = "-moz-border-radius: 200px;"></center>" '
    flash("you are now logged in as %s" % login_session['username'])
    print("Done")
    return output


# Create New User
def createUser(login_session):
    newUser = User(name=login_session['username'],
                   email=login_session['email'])
    session.add(newUser)
    session.commit()

    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


# Getting information of user
def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


# Getting user email address
def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except Exception as e:
        return None


# To read director JSON data on web browser
@app.route('/director/JSON')
def directorJSON():
    director = session.query(Director).all()
    return jsonify(director=[c.serialize for c in director])


# To read director wise of movie JSON
@app.route('/director/<int:director_id>/menu/<int:movie_id>/JSON')
def directorListJSON(country_id, player_id):
    Movie_List = session.query(Movie).filter_by(id=movie_id).one()
    return jsonify(Movie_List=Movie_List.serialize)


# To read movie JSON
@app.route('/director/<int:movie_id>/menu/JSON')
def movieListJSON(player_id):
    director = session.query(Director).filter_by(id=movie_id).one()
    movie = session.query(Movie).filter_by(Movie_id=director.id).all()
    return jsonify(MovieLists=[i.serialize for i in movie])


# This is a home page of entire project
@app.route('/director/')
def showDirector():
    director = session.query(Director).all()
    return render_template('director.html', director=director)


# Create new Director
@app.route('/director/new/', methods=['GET', 'POST'])
def newDirector():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newDirector = Director(name=request.form['name'],
                             user_id=login_session['user_id'])
        session.add(newDirector)
        session.commit()
        return redirect(url_for('showDirector'))
    else:
        return render_template('newDirector.html')


# To Edit existing director name
@app.route('/director/<int:director_id>/edit/', methods=['GET', 'POST'])
def editDirector(director_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedDirector = session.query(Director).filter_by(id=director_id).one()
    creater_id = getUserInfo(editedDirector.user_id)
    user_id = getUserInfo(login_session['user_id'])
    if creater_id.id != login_session['user_id']:
        flash("You cannot edit this Director "
              "This is belongs to %s" % (creater_id.name))
        return redirect(url_for('showDirector'))
    if request.method == 'POST':
        if request.form['name']:
            editedDirector.name = request.form['name']
            flash("Director Successfully Edited %s" % (editedDirector.name))
            return redirect(url_for('showDirector'))
    else:
        return render_template('editDirector.html', director=editedDirector)



# To Delete existing Director
@app.route('/director/<int:director_id>/delete/', methods=['GET', 'POST'])
def deleteDirector(director_id):
    if 'username' not in login_session:
        return redirect('/login')
    directorToDelete = session.query(Director).filter_by(id=director_id).one()
    creater_id = getUserInfo(directorToDelete.user_id)
    user_id = getUserInfo(login_session['user_id'])
    if creater_id.id != login_session['user_id']:
        flash("You cannot delete this Director "
              "This is belongs to %s" % (creater_id.name))
        return redirect(url_for('showDirector'))
    if request.method == 'POST':
        session.delete(directorToDelete)
        flash("Successfully Deleted %s" % (directorToDelete.name))
        session.commit()
        return redirect(url_for('showDirector', director_id=director_id))
    else:
        return render_template('deleteDirector.html', director=directorToDelete)


# It Displays the total movie list of particular director
@app.route('/director/<int:director_id>/movies')
def showMovies(director_id):
    director = session.query(Director).filter_by(id=director_id).one()
    movie = session.query(Movie).filter_by(movie_id=director_id).all()
    return render_template('menu.html', director=director, movie=movie)


# Creating new movie
@app.route('/director/<int:movie_id>/new/', methods=['GET', 'POST'])
def newMovieList(movie_id):
    if 'username' not in login_session:
        return redirect('login')
    director = session.query(Director).filter_by(id=movie_id).one()
    creater_id = getUserInfo(director.user_id)
    user_id = getUserInfo(login_session['user_id'])
    if creater_id.id != login_session['user_id']:
        flash("You cannot add this movie "
              "This is belongs to %s" % (creater_id.name))
        return redirect(url_for('showDirector', director_id=movie_id))
    if request.method == 'POST':
        newList = Movie(name=request.form['name'],
                         description=request.form['description'],
                         actor=request.form['actor'],
                         actress=request.form['actress'],
                         release=request.form['release'],
                         movie_id=movie_id,
                         user_id=login_session['user_id'])
        session.add(newList)
        session.commit()
        flash("New Movie List %s is created" % (newList))
        return redirect(url_for('showMovies', director_id=movie_id))
    else:
        return render_template('newmovielist.html', movie_id=movie_id)




# Editing to particular director movie
@app.route('/director/<int:director_id>/<int:p_id>/edit/',
           methods=['GET', 'POST'])
def editMovieList(director_id, p_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedList = session.query(Movie).filter_by(id=p_id).one()
    director = session.query(Director).filter_by(id=director_id).one()
    creater_id = getUserInfo(editedList.user_id)
    user_id = getUserInfo(login_session['user_id'])
    if creater_id.id != login_session['user_id']:
        flash("You cannot edit this Director "
              "This is belongs to %s" % (creater_id.name))
        return redirect(url_for('showMovies', director_id=director_id))
    if request.method == 'POST':
        editedList.name = request.form['name']
        editedList.description = request.form['description']
        editedList.actor = request.form['actor']
        editedList.actress = request.form['actress']
        editedList.release = request.form['release']
        session.add(editedList)
        session.commit()
        flash("Movie List has been edited!!")
        return redirect(url_for('showMovies', director_id=director_id))
    else:
        return render_template('editmovielist.html',
                               director=director, movie=editedList)


# Deleting particular director of movie
@app.route('/director/<int:movie_id>/<int:list_id>/delete/',
           methods=['GET', 'POST'])
def deleteMovieList(player_id, list_id):
    if 'username' not in login_session:
        return redirect('/login')
    director = session.query(Director).filter_by(id=movie_id).one()
    listToDelete = session.query(Player).filter_by(id=list_id).one()
    creater_id = getUserInfo(listToDelete.user_id)
    user_id = getUserInfo(login_session['user_id'])
    if creater_id.id != login_session['user_id']:
        flash("You cannot edit this Director "
              "This is belongs to %s" % (creater_id.name))
        return redirect(url_for('showMovies', director_id=movie_id))
    if request.method == 'POST':
        session.delete(listToDelete)
        session.commit()
        flash("Movie list has been Deleted!!!")
        return redirect(url_for('showMovies', director_id=movie_id))
    else:
        return render_template('deletemovielist.html', lists=listToDelete)


# Logout from application
@app.route('/disconnect')
def logout():
    access_token = login_session['access_token']
    print("In gdisconnect access token is %s", access_token)
    print("User Name is:")
    print(login_session['username'])

    if access_token is None:
        print("Access Token is None")
        response = make_response(json.dumps('Current user not connected.'),
                                 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = login_session['access_token']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = \
        h.request(uri=url, method='POST', body=None,
                  headers={'content-type':
                           'application/x-www-form-urlencoded'})[0]

    print(result['status'])
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        flash("Successfully logged out")
        return redirect(url_for('showDirector'))
    else:
        response = make_response(
            json.dumps('Failed to revoke token for given user.'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5050)








     
