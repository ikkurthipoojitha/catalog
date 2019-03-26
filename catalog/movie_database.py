import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Store=declarative_base()

class User(Store):
     __tablename__ = 'user'
     id = Column(Integer,primary_key=True)
     name = Column(String(100),nullable=False)
     email = Column(String(100),nullable=False)

     


class Director(Store):
     __tablename__ = 'director'
     id = Column(Integer,primary_key=True)
     name = Column(String(100), nullable=False)
     user_id = Column(Integer, ForeignKey('user.id'))
     user = relationship(User)
    



     @property
     def serializable(self):
          return {
               'id' : self.id,
               'name' : self.name
               }

     
class Movie(Store):
     __tablename__ = 'movie'
     id = Column(Integer, primary_key=True)
     name = Column(String(100), nullable=False)
     description = Column(String(2000))
     actor = Column(String(100))
     actress = Column(String(100))
     release = Column(Integer)
     movie_id = Column(Integer, ForeignKey('director.id'))
     director = relationship(Director)
     user_id = Column(Integer, ForeignKey('user.id'))
     user = relationship(User)


     @property
     def serializable(self):
          return {
               'id' : self.id,
               'name' : self.name,
               'description' : self.description,
               'actor' : self.actor,
               'actress' : self.actress,
               'release' : self.release,
               'movie_id' : self.movie_id
               }
     
engine = create_engine('sqlite:///movie_database.db')

Store.metadata.create_all(engine)

