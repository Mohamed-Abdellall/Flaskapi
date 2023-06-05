# -- Import section --
from flask import Flask
from flask import render_template, request, redirect
from pymongo import MongoClient

# -- INITIALIZE APP --
app = Flask(__name__)

# CONFIGURE MONGO DB
# create the clent
username = "user"
password = "pass"
url = f"your URL {username} {password}"
client = MongoClient(url)

# our database manager object
db = client["your DB name"]

# CRUD Operations
# collection = db.events
# event = {
# "name" : "Powerwashing my Turtle"
# "date" : "2020-03-12"
# }
# CREATE

# READ

# UPDATE

# DELETE


# HOME PAGE
@app.route("/")
@app.route("/home")
def show_board():
  return render_template("index.html")


# HANDLE POST AND GET for a NEW EVENT
@app.route("/new")
def new_event():
  return render_template("form.html")


# CLEAR OUT THE EVENTS
# @app.route("/clear")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
