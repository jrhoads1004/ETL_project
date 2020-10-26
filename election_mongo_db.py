import os
import json
import pymongo
from pymongo import MongoClient
from pprint import pprint
import datetime
from flask import Flask, render_template

# Create an instance of our Flask app.
app = Flask(__name__)

# The default port used by MongoDB is 27017
# https://docs.mongodb.com/manual/reference/default-mongodb-port/
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Declare the database
db = client.election_db
candidate_collection = db.candidate

# Drops collection if available to remove duplicates
# NOTE: This is only for demo purposes.
#db.candidate.drop()

csvpath = os.path.join("Resources", "popular_votes_years.csv")

with open(csvpath) as datafile:
    file_data = csv.load(datafile)

if isinstance(file_data, list): 
    candidate_collection.insert_many(file_data)   
else: 
    candidate_collection.insert_one(file_data) 

csvpath = os.path.join("Resources", "candidate_finance_2.csv")

with open(csvpath) as datafile:
    finance_data = csv.load(datafile)

if isinstance(finance_data, list): 
    candidate_collection.insert_many(finance_data)   
else: 
    candidate_collection.insert_one(finance_data) 

# Set route
@app.route('/')
def index():
    # Store the entire team collection in a list
    Name = list(candidate_collection.find())
    print(Name)

    # Return the template with the players list passed in
    return render_template('index.html', Name=Name)

# Define route to insert new players into the database
@app.route('/insert/<name>/<Votes>/<VotePct>/<year>')
def insert(Name, Votes, VotePct, year):
    new_candidate_vote = {
                            'name': Name, 
                            'Votes': Votes,
                            "VotePct": VotePct,
                            "year": year
                         }
    
    db.insert_one(new_candidate_vote)
    return f"{name} has been inserted into the database!"

if __name__ == "__main__":
app.run(debug=True)
  

