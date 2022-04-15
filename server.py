"""Server for movie ratings app."""

from crypt import methods
from flask import (Flask, render_template, request, flash, session, 
                  redirect)

from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """ A Homepage. """

    return render_template('homepage.html')

@app.route('/movies')
def all_movies():
    """View all movies."""

    # call function from crud to get all movies
    movies = crud.get_movies()

    # rendering and pass in the list of movies
    return render_template("all_movies.html", movies=movies)

@app.route("/movies/<movie_id>")
def show_movie(movie_id):
    """Show details on a particular movie"""

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)

@app.route("/users")
def all_users():
    """View all users."""

    users= crud.get_users()

    return render_template("all_users.html", users=users)

@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password= request.form.get("password")

    user = crud.get_user_by_email(email)
    # check if the user's email is already registered
    # then flash a message and say can't create an account
    # with that email
    if user:
       flash("You cannot create an account with this email. Please try again!") 
    else:
        user = crud.create_user(email, password) 

        flash("Account successfully created!")
    return redirect("/")

@app.route("/users/<user_id>")
def show_user(user_id):
    """Show details in a particular user."""
    # before to create the variable user 
    # we created a crud function
    user= crud.get_user_by_id(user_id)

    return render_template("user_details.html", user=user)

@app.route("/login", methods=["POST"])
def login():
    """ Processing user login."""

    email= request.form.get("email")
    password =request.form.get("password")

    user = crud.get_user_by_email(email)

    if not user or user.password != password:
        flash("The email or password is incorrect.")
    else:
        
        # session["user_id"] = user.user_id

        session["user_email"] = user.email
        flash(f"Welcome back, {user.email}!")

    return redirect("/")


















# Replace this with routes and view functions!


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
