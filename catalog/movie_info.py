from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from movie import User,Store,Director,Movie
engine=create_engine('sqlite:///movie_database.db')


Store.metadata.bind = engine

DBSession = sessionmaker(bind=engine)


session = DBSession()

#Sample User
User1 = User(
     name = "Poojitha Ikkurthi",
     email = "ipoojitha1997@gmail.com",
     )
session.add(User1)
session.commit()



#Menu (list of movies) for Rajamouli
director1 = Director(name = "Rajamouli", user_id = 1)
session.add(director1)
session.commit()


#Baahubali1 movie info
movie1=Movie(name = "Baahubali: The Conclusion",
             description = "Kattappa continues to narrate how he ended up killing Amarendra Baahubali."
                            "After vanquishing the Kalakeyas Amarendra Baahubali is declared as the future king of Mahishmati and Bhallaladeva its commander in chief."
                            "The Rajamatha Sivagami orders Amarendra to tour the kingdom and its neighbourhood along with Kattappa.",
             
             actor = "Prabhas",
             actress = "Anushkha",
             release = 2015,
             movie_id = 1,
             user_id = 1
             )
session.add(movie1)
session.commit()
                            
#Baahubali2 movie info
movie2=Movie(name = "Baahubali: The Beginning",
             description = "In the ancient kingdom of Mahishmathi a woman carrying a baby falls into a waterfall and breathes her last but before dying she holds the baby in one hand above her head."
                            "The baby is rescued by local villagers and adopted by Sanga and her husband. Named Shivudu he grows up to be a strong adventurous young man who is curious about the waterfall and the land beyond."
                            "After finding a wooden mask on the ground he is driven to find the owner of the mask and succeeds in climbing the waterfall.",
             actor = "Prabhas",
             actress = "Anushkha",
             release = 2017,
             movie_id = 1,
             user_id = 1
             )
session.add(movie2)
session.commit()
#Magadheera  movie info
movie3 = Movie(name = "Magadheera ",
               description = "Harsha a bike racer is taking an auto rickshaw to the airport in the rain."
                              "He spots the blurry outline of a woman trying to flag the auto down and gestures to her that it is already occupied."
                              "As he does their fingers accidentally touch and Harsha feels an electric current passing through him which triggers a few fleeting images."
                              "Later feeling that this was the girl he was destined to be with he enquires about her to a woman named Indira without realising that she is the same girl",
               actor = "Ram charan",
               actress = "Kajal Aggarwal",
               release = 2009,
               movie_id = 1,
               user_id = 1
               )
session.add(movie3)
session.commit()
               
#Eega  movie info
movie4 = Movie(name = "Eega",
               description = "Nani is a young man who specialises in preparing fireworks. He is in love with his neighbour Bindu a micro artist who runs Project  a non-governmental organisation."
                              "Seeking to raise money for her Bindu visits the office of a rich powerful industrialist named Sudeep who also finds her attractive."
                              "He befriends her donates huge amout of money and gains her trust. Sudeep sees Nani as a rival and plans to kill him."
                              "One night Nani helps Bindu to finish a piece of micro art a locket made from a pencil. While returning home, he is kidnapped by Sudeep, who kills him making his death look like an accident."
                              "Unaware of the incident Bindu proposes to the dying Nani by telephone it is the last thing Nani hears before he is reincarnated as a housefly that cannot remember its previous life.",
               actor = "Nani",
               actress = "Samantha Ruth Prabhu",
               release = 2012,
               movie_id = 1,
               user_id = 1
               )
session.add(movie4)
session.commit()
#Sye  movie info
movie5 = Movie(name = "Sye",
               description = "Prudhvi and Shashank  are the leaders of two warring student groups in a Hyderabad college."
                              "They are fond of rugby union game and they sort things out between them by playing rugby to prove superiority."
                              "One day a local mafia leader Bhikshu Yadav  gets a court notice that he has purchased the land of college from its legal heirs."
                              "Prudhvi and Sashank groups unite by forgetting their differences to win back the land for the college.",
               actor = "Nithiin",
               actress = "Genelia Deshmukh",
               release = 2004,
               movie_id = 1,
               user_id = 1
               )
session.add(movie5)
session.commit()

#Chatrapathi  movie info
movie6 = Movie(name = "Chatrapathi",
               description = "Shivaji and Ashok are the sons of Parvati. Shivaji is her stepson but Parvati shows equal affection on both of them. This is not liked by Ashok her biological son."
                              "The port is dominated by Baji Rao and some goons using refugee labor for their own gain. Shivaji is an aggressive guy but is controlled by his well wishers."
                              "One day he reacts aggressively in defense of himself and the other refugees. People start calling him Chatrapathi.",
               actor = "Prabhas",
               actress = "Shriya Saran",
               release = 2005,
               movie_id = 1,
               user_id = 1
               )
session.add(movie6)
session.commit()

#Yamadonga  movie info
movie7 = Movie(name = "Yamadonga ",
               description = "Raja an orphan boy, is a thief. Mahi young girl falls in love with him."
                              "Raja manipulates her by gaining her sympathy."
                              "She gives him a necklace which he throws away because it is worthless however it always comes back to him.",
               actor = "Nandamuri Taraka Rama Rao Jr",
               actress = "Priyamani",
               release = 2007,
               movie_id = 1,
               user_id = 1
               )
session.add(movie7)
session.commit()
#Vikramarkudu  movie info
movie8 = Movie(name = "Vikramarkudu ",
               description = "Athili Sathi Babu is a rookie thief in Hyderabad who is crazy about performing dare devil acts."
                              "He falls in love with Neeraja who is in Hyderabad to attend a marriage."
                              "Sathi Babu tells her the truth about him being a thief and resolves to give up crime forever. "
                              "But before that he decides to swindle one last person for a large sum of money along with his con friend Duvva",
               actor = "Raviteja",
               actress = "Anushka Shetty",
               release = 2006,
               movie_id = 1,
               user_id = 1
               )
session.add(movie8)
session.commit()

#Simhadri  movie info
movie9 = Movie(name = "Simhadri",
               description = "An orphan and good-hearted lad Simhadri is adopted and grows up under Ram Bhupal Varma family care in Visakhapatnam."
                              "The bond they share is like father and son. Kasturi  is Varmas granddaughter, and she likes Simhadri a lot."
                              "Once a week Simhadri visits a mentally challenged girl called Indu."
                              "He entertains her and provides money to her caretakers",
               actor = "Nandamuri Taraka Rama Rao Jr",
               actress = "Bhumika Chawla",
               release = 2003,
               movie_id = 1,
               user_id = 1
               )
session.add(movie9)
session.commit()

#Student No.1 movie info
movie10 = Movie(name = "Student No.1",
               description = "Aditya joins a law college in Vizag as a student. The college is notorious for its unruly students headed by Satya."
                              "Aditya is shown as a mysterious young man and throughout the first half there are flashbacks to his story."
                              "He makes the unruly students mend their ways."
                              "In the interval we come to know that Aditya is a criminal facing murder charges and is serving his life term in Vizag central jail.",
               actor = "Nandamuri Taraka Rama Rao Jr",
               actress = "Gajala",
               release = 2001,
               movie_id = 1,
               user_id = 1
               )
session.add(movie10)
session.commit()

#Maryada Ramanna movie info
movie11 = Movie(name = "Maryada Ramanna",
               description = "Faction feud in Rayalseema results in the death of Ramineedus brother and he along with his two sons Mallasuri and Baireddy vow for revenge."
                              "Time turns 28 years and comes to Hyderabad."
                              "Here lives Ramu an innocent and somewhat unlucky guy whose parents are no more and is ousted out of his job.",              
               actor = "Sunil",
               actress = "Saloni Aswani",
               release = 2010,
               movie_id = 1,
               user_id = 1
               )
session.add(movie11)
session.commit()

#Menu (list of movies) for Sukumar
director2 = Director(name = "Sukumar", user_id = 1)
session.add(director2)
session.commit()

#Rangasthalam  movie info
movie1 = Movie(name = "Rangasthalam ",
               description = "The film begins with Chitti Babu  rescuing MLA Dakshina Murthy  from a seemingly fatal road accident."
                              "The story then shifts to a village Rangasthalam. Chitti Babu is a partially deaf lighthearted jolly villager who earns a living by watering irrigational lands of the farmers of Rangasthalam using a motor which belongs to another villager and his best friend Rangamma who he fondly calls Rangamma Atta."
                              "Chitti Babu is in love with Ramalakshmi the daughter of the village drunkard."
                              "Rangasthalam is shown to be run by President Phanindra Bhoopathi  an influential cruel landlord who runs the Society which lends loans to farmers but notes down higher amounts in records and extracts high amounts from poor farmers.",
               actor = "Ram Charan",
               actress = "Samantha Akkineni",
               release = 2018,
               movie_id = 2,
               user_id = 1
               )
session.add(movie1)
session.commit()

#1: Nenokkadine movie info
movie2 = Movie(name = "1: Nenokkadine",
               description = "1: Nenokkadine revolves around the search by Gautham  for his parents whom he believes were murdered by three men."
                              "Sameera a journalist convinces him that he is an orphan and is hallucinating."
                              "When Gautham kills one of the imaginary men for his psychological satisfaction he realises that the dead man is real and leaves for London to find his roots and the other two men behind his parents death",
               actor = "Mahesh Babu",
               actress = "Kriti Sanon",
               release = 2014,
               movie_id = 2,
               user_id = 1
               )
session.add(movie2)
session.commit()

#Nannaku Prematho movie info
movie3 = Movie(name = "Nannaku Prematho",
               description = "Abhiram the youngest son of London-based Subramanyam  quits his job and starts his own company KMC Pipes and Canals."
                              "He comes to know that his father is suffering from pancreatic cancer and has roughly a month or more to live."
                              "Subramanyam reveals his name as Ramesh Chandra Prasad one of Londons richest entrepreneurs who lost all his wealth because of a cunning man Krishnamurthy Kautilya who made his empire cheating Ramesh Chandra",
               actor = "Nandamuri Taraka Rama Rao Jr",
               actress = "Rakul Preet Singh",
               release = 2016,
               movie_id = 2,
               user_id = 1
               )
session.add(movie3)
session.commit()

#Aarya  movie info
movie4 = Movie(name = "Aarya",
               description = "Geetha  a college student goes to Kanyakumari on a trip."
                              "She finds a poem in a diary left on a beach and signs in it, saying that she wishes the poet will succeed in his love."
                              "Later on her anklet falls into the ocean and a guy jumps into the water in front of her eyes but no one sees him resurfacing. However Geetha did not see who jumped in the ocean."
                              "She dreams about the incident frequently with the idea that the guy who jumped has died but her friends ask her to forget it.",
               actor = "Allu Arjun",
               actress = "Anuradha Mehta",
               release = 2004,
               movie_id = 2,
               user_id = 1
               )
session.add(movie4)
session.commit()
#Kumari 21F movie info
movie5 = Movie(name = "Kumari 21F",
               description = "Siddhu is a chef leading a middle class life with his mother in colony."
                              "His father Ravikanth is accused of having an extra marital affair that leads to the separation of his parents."
                              "Siddhu aims to be a chef on a cruise liner in Singapore and his financial status does not support him."
                              "His friends Shankar Srinu and Suresh steal money from people who use the local ATM they hide in some local ruins for three days and Siddhu cooks for them and provides liquor receiving a share of the money in return.",
               actor = "Raj Tarun",
               actress = "Hebah Patel",
               release = 2015,
               movie_id = 2,
               user_id = 1
               )
session.add(movie5)
session.commit()
#100% Love movie info
movie6 = Movie(name = "100% Love",
               description = "Balu is always the top ranker in his college. Mahalakshmi his cousin comes to Balus house to continue her studies."
                              "She is in awe of her Mr. Perfect Bava and takes his help to achieve big in studies. Surprisingly she surpasses him and becomes the first ranker."
                              "Balu gets deeply hurt by this and he resorts to cunning ways to deviate Mahalakshmi. But to his surprise Ajith stands first this time."
                              "Meanwhile Mahalakshmis father brings her a marriage proposal but she doesnot want to marry him. Balu and Mahalakshmi compromise by agreeing to help each other."
                              "Balu helps her in getting the proposal canceled and Mahalakshmi starts deviating Ajith from studies for the sake of Balu but Balu gets attracted to her.",
               actor = "Naga Chaitanya",
               actress = "Tamannaah",
               release = 2011,
               movie_id = 2,
               user_id = 1
               )
session.add(movie6)
session.commit()
#Arya 2 movie info
movie7 = Movie(name = "Arya 2",
               description = "The film opens dramatically with Arya  being carried into an operation theatre. His friend Ajay narrates how Arya changed his life. In their childhood Arya stays in an orphanage where he has no friends or family."
                              "By force he befriends Ajay who also is in that orphanage. From an early age Arya displays an unusual psychology which sets him apart from the rest of the kids."
                              "He is unnaturally possessive about Ajay. However Ajay is not too fond of his friend",
               actor = "Allu Arjun",
               actress = "Kajal Aggarwal",
               release = 2009,
               movie_id = 2,
               user_id = 1
               )
session.add(movie7)
session.commit()
#Jagadam  movie info
movie8 = Movie(name = "Jagadam",
               description = "When all the boys wanted to become engineers doctors lawyers and other professions Seenu wanted to become a goonda."
                              "Though he behaves like a ruffian he comes to know that one should have the support of a politician or big dada."
                              "With the help of Laddu  an associate of Manikyam Seenu meets the latter and joins his gang. At this juncture Seenu falls in love with Subbalakshmi",
               actor = "Ram",
               actress = "Isha Sahani",
               release = 2007,
               movie_id = 2,
               user_id = 1
               )
session.add(movie8)
session.commit()

#Menu (list of movies) for Gunasekhar
director3 = Director(name = "Gunasekhar", user_id = 1)
session.add(director3)
session.commit()

#Rudhramadevi  movie info
movie1 = Movie(name = "Rudhramadevi",
               description = "Ganapatideva  is the emperor of the Kakatiya dynasty who rules Kakatiya Empire from Orugallu  as its capital city. There are only two threats to Ganapatis rule. Murari Devudu and Hari Hara Devudu  dukes of Kakatiya are both obviously unsatisfied with Ganapatis reign and plot to usurp the throne."
                              "Emperor Singhana of the Devagiri Empire also wishes to conquer the Kakatiyas and name his grandson and heir Mahadeva as king. Meanwhile Ganapatis wife is pregnant.",
               actor = "Rana Daggubati",
               actress = "Anushkha shetty",
               release = 2015,
               movie_id = 3,
               user_id = 1
               )
session.add(movie1)
session.commit()
#Okkadu  movie info
movie2 = Movie(name = "Okkadu",
               description = "Ajay Varma  is a Hyderabad-based Kabbadi player who visits Kurnool to take part in a state-level tournament. There he saves Swapna Reddy  from Obul Reddy a dangerous faction leader who is in love with Swapna and wants to marry her against her wishes."
                              "Ajay learns that Swapna is trying to leave to the United States for pursuing higher education after Obul killed her brothers."
                              "When Ajay saves Swapna he humiliates Obul by pushing him into a mudpond. Obul refuses to cleanse the mud until Swapna is found and brought back. Ajay helps Swapna escape and takes her to his house in an old city hiding her in his room with the help of his sister",
               actor = "Mahesh Babu",
               actress = "Bhoomika Chawla",
               release = 2003,
               movie_id = 3,
               user_id = 1
               )
session.add(movie2)
session.commit()

#Varudu movie info
movie3 = Movie(name = "Varudu ",
               description = "Sandeep is a next-gen youngster who parties hard and has a modern outlook but his ideas towards marriage are traditional. As he gets a job in the USA his parents Vasundhara and Raj Gopal who got married against their respective parents wishes ask him to get married."
                              "He accepts and tells them that he will marry a girl of their choice in a ceremony that lasts five days. He also refuses to see his bride until the marriage."
                              "Everything is arranged according to his wishes and his marriage is fixed with Deepthi . At the ceremony when Sandy and Deepthi see each other they fall in love at first sight.",
               actor = "Allu Arjun",
               actress = "Bhanu Sri Mehra",
               release = 2010,
               movie_id = 3,
               user_id = 1
               )
session.add(movie3)
session.commit()


#Nippu movie info
movie4 = Movie(name = "Nippu",
               description = "The story begins with Surya who owns a gym center and has a good friend named Sriram Surya is in love with Srirams sister Meghna  and after some cat and mouse games  she also falls in love with Surya. After a while Sriram goes to Saudi Arabia for a job and falls in love with Vaishnavi. The story takes a turn when Surya also goes to Saudi Arabia to celebrate Srirams birthday and is shocked when the police arrests Sriram on charges of murdering Vaishnavi. He is sentenced to death."
                              "The only thing Surya can do is get the signature from Vaishnavis parents to acquit Sriram but Vaishnavis father is Raja Goud the bad guy whom Surya has been fighting all along. What happens from there forms the rest of the story.",
               actor = "Ravi Teja",
               actress = "Deeksha Seth",
               release = 2012,
               movie_id = 3,
               user_id = 1
               )
session.add(movie4)
session.commit()

#Arjun movie info
movie5 = Movie(name = "Arjun",
               description = "Arjun and his twin sister Meenakshi finish college and their parents decide to look for a good man to marry Meenakshi."
                              "Meenakshi shows Arjun a letter from their friend Uday who confesses his love for her and asks her to elope with him as his parents Bala Nayagar and Andal are arranging his marriage with a different girl."
                              "Meenakshi tells Arjun that she too is interested in Uday.",
               actor = "Mahesh Babu",
               actress = "Shriya Saran",
               release = 2004,
               movie_id = 3,
               user_id = 1
               )
session.add(movie5)
session.commit()

print("List of Players are added!!!")

