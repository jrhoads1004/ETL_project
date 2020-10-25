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
# db.candidate.drop()

jsonpath = os.path.join("Resources", "popular_votes_years.json")

with open(jsonpath) as datafile:
    file_data = json.load(datafile)

if isinstance(file_data, list): 
    candidate_collection.insert_many(file_data)   
else: 
    candidate_collection.insert_one(file_data) 

jsonpath = os.path.join("Resources", "candidate_finance_2.json")

with open(jsonpath) as datafile:
    finance_data = json.load(datafile)

if isinstance(finance_data, list): 
    candidate_collection.insert_many(finance_data)   
else: 
    candidate_collection.insert_one(finance_data) 

# Set route
@app.route('/')
def index():
    # Store the entire team collection in a list
    Name = list(db.name.find())
    print(Name)

#     # Return the template with the players list passed in
#     return render_template('index.html', Name=Name)

# Define route to insert new players into the database
@app.route('/insert/<name>/<position>')
def insert(Name, Votes, VotePct, year):
    new_candidate = {
                    'name': Name, 
                    'Votes': Votes,
                    "VotePct": VotePct,
                    "year": year
                  }
    
    db.insert_one(new_candidate)
    return f"{name} has been inserted into the database!"

    

# # Ask the user for input. Store information into variables.
# # Note: the '\n' in the print statement below just prints an empty line in our terminal before printing our text.
# print("\nPlease provide input.")
# print("-"*30)

# year = input('Election Year: ')
# candidate_name = input("Candidate Name")
# political_party = input('REPUBLICAN or DEMOCRATIC: ')
# candidate_id = input('Candidate ID: ')
# vote_total = input('Popular Vote Total: ')
# per_pop_vote_total = input("Percent of Popular Vote:  ")

# # A dictionary that will become a MongoDB document
# #post = {
#    # 'Year': year,
#   #  'REPUBLICAN or DEMOCRATIC': political_party,
#   #  "Candidate ID": candidate_id,
#   #  'Popular Vote Total': vote_total,
#   #  "Percent of Popular Vote": per_pop_vote_total,
#   #  'date': datetime.datetime.utcnow()
# #}

# # Insert document into collection
# #collection.insert_one(post)

# print("\n\nThank you! Your entry has been added to the database.")

# # Verify results:
# results = collection.find(post)
# for result in results:
#     pprint(result)
