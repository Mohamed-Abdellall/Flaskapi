# -- Import section --
from flask import Flask
from flask import render_template, request, redirect
from pymongo import MongoClient

# -- INITIALIZE APP --
app = Flask(__name__)

# CONFIGURE MONGO DB
# create the clent
username = "events"
password = "lGlIsfSP6WyqWibq"
url = f"mongodb+srv://events:{password}@cluster0.naxhknz.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)

# our database manager object
db = client["database"]

# CRUD Operations
collection = db.events
event = {"name": "Powerwashing my Turtle", "date": "2020-03-12"}
# CREATE
collection.insert_one(event)

# READ
# collection.find({})
# db_query = "Powerwashing my Turtle"
# collection.find({"name" : db_query})

# UPDATE
# new_value = {"$set" : {"name" : "Powerwashing my Child"}}
# collection.update_one(db_query, new)

# DELETE
# collection.delete_one(db_query)


# HOME PAGE
@app.route("/")
@app.route("/home")
def show_board():
  collection = db.events
  events = collection.find({})
  return render_template("index.html", events=events)


# HANDLE POST AND GET for a NEW EVENT
@app.route("/new", methods=["POST", "GET"])
def new_event():
  if (request.method == "POST"):
    # our collection
    collection = db.events
    event = {"name": request.form["name"], "date": request.form["date"]}
    collection.insert_one(event)
    return redirect("/home")
  else:
    return render_template("form.html")


# CLEAR OUT THE EVENTS
@app.route("/clear", methods=["POST"])
def clear_events():
  collection = db.events
  collection.delete_many({})
  return render_template("index.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
