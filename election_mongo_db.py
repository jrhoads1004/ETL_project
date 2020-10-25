import pymongo
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

# Drops collection if available to remove duplicates
# NOTE: This is only for demo purposes.
db.candidates.drop()

db.candidates.insert_one(
    [
        {
            'name': 'Donald Trump',
            'political_party': 'REPUBLICAN'
        }    
    ]
)    
    
#     [
#         {
#             "year": "Year",
#             "political_party": 'REPUBLICAN or DEMOCRATIC', 
#             "candidate_id": "Candidate ID", 
#             "vote_total": "PopularVote Total",  
#             'date': datetime.datetime.utcnow()
#         }
#     ]
# )

# # Creates a collection in the database and inserts one document
# db.candidates.insert_one(
#     [
#         {
#             "year": "Year",
#             "political_party": 'REPUBLICAN or DEMOCRATIC', 
#             "candidate_id": "Candidate ID", 
#             "vote_total": "PopularVote Total",  
#             'date': datetime.datetime.utcnow()
#         }
#     ]
# )


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
