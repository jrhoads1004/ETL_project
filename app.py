import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, and_
from flask import Flask, render_template
import pymongo

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

# Create variable for the connection string
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.election_db

# Pass connection string to the pymongo instance.
candidate_collection = db.candidate

#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    candidate_info = list(candidate_collection.find())
    print(candidate_info)

    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", candidate_info=candidate_info)

if __name__ == "__main__":
    app.run(debug=True)