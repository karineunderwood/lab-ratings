"""Script to seed database."""
import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb ratings")
os.system("createdb ratings")

model.connect_to_db(server.app)
model.db.create_all()



with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# movie_data is now a list of dictionaries (python)
# loop over each dict in the list movie_data
# use to supply arguments to crud.create_movie
# add each new movie to a list
# to create fake ratings later
movies_in_db=[]
for movie in movie_data:
    # we are unpacking the dict
    title, overview, poster_path = (
        movie['title'],
        movie['overview'],
        movie['poster_path'],
    )
    # here we got the release_date and converted to a datetime 
    # object with the (datetime.strptime)
    release_date = datetime.strptime(movie['release_date'], "%Y-%m-%d")
    # we created a movie
    db_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(db_movie)

# here we have to go through model 
# before you can access db.
model.db.session.add_all(movies_in_db)
model.db.session.commit()

# create 10 users and each user will make 10 ratings
for n in range(10):
    email = f'user{n}@test.com'
    password = 'test'

    # create a user - the order is: instantiate, add and commit
    user = crud.create_user(email, password)
    model.db.session.add(user)

    for rt in range(10):
        # we created a random_movie variable 
        # and used the choice function from random module
        # to pick a random movie (refered to line 60)
        random_movie = choice(movies_in_db)
        # we created a score variable
        # and then used the randint function from random module
        score = randint(1,5)
        # 1st initialize
        rating = crud.create_rating(user, random_movie, score)
        # 2nd add
        model.db.session.add(rating)
# 3rd commit
model.db.session.commit()

# when we run seed_database.py we get a list of score, movie id and user id 

