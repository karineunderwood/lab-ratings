"""CRUD operations."""
# Initiaze the first steps.
# Always create a docstring to inform what the file is about.
# then import the requirements.
# we imported the classes we already created on model.py.
from model import db, User, Movie, Rating, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user
    
def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie"""

    movie = Movie(title = title, overview=overview, release_date=release_date, poster_path=poster_path)
    
    return movie

def get_movies():
    """ Return all movies."""

    return Movie.query.all()


def create_rating(user, movie, score):
    """ Create and return a new rating"""

    rating = Rating(user=user, movie=movie,score=score)

    return rating


def get_movie_by_id(movie_id):
    """Return movie by id(pk)."""

    return Movie.query.get(movie_id)


def get_users():
    """Return all users."""

    return User.query.all()

def get_user_by_id(user_id):
    """Return user by id(pk)."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return user by email."""


    return User.query.filter(User.email == email).first()




# Always make sure to use this at the bottom
# we are importing Flask app = Flask(__name__)

if __name__ == '__main__':
    from server import app
    connect_to_db(app)