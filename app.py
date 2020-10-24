import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, and_

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine('postgresql://postgres:********@localhost:5432/election_db')

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

# Save reference to the table
Candidate_Name = Base.classes.candidate_name
Candidate_Finance = Base.classes.candidate_finance
Candidate_Votes = Base.classes.candidate_votes

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available routes."""
    return (
        f"Available Routes:<br/>"
        f"/YEAR<br/>"
        f"/candidates<br/>"
        f"/years<br/>"
        f"/financial_votes<br/>"
    )

@app.route("/<year>")
def summary(year):
    """Return a list of all candidates financial data and election results for that year"""

    # Open a communication session with the database
    session = Session(engine)

    results = session.query(Candidate_Finance.election_year, Candidate_Name.first_name, Candidate_Name.last_name, Candidate_Name.party,  Candidate_Finance.total_receipts, Candidate_Finance.total_disbursements, Candidate_Finance.cash_on_hand, Candidate_Votes.total_vote, Candidate_Votes.percentage).\
        filter(candidate_finance.election_year == year).\
        order_by(Candidate_Votes.total_vote).all()
    
    # Convert the query results to a dictionary 
    year_list = []
    for candidate in results:
        year_dict = {}
        year_dict["election_year"] = election_year
        year_dict["first_name"] = first_name
        year_dict["last_name"] = last_name
        year_dict["party"] = party
        year_dict["total_receipts"] = total_receipts
        year_dict["total_disbursements"] = total_disbursements
        year_dict["cash_on_hand_end_period"] = cash_on_hand
        year_dict["popular_vote_total"] = total_vote
        year_dict["percent_popular_vote"] = percentage
        year_list.append(year_dict)

    # close the session to end the communication with the database
    session.close()

    # Return the JSON representation of the dictionary
    return jsonify(year_list)

if __name__ == '__main__':
    app.run(debug=True)

# @app.route("/candidates")
# def candidates():
#     """Return a list of candidates that have ran for president"""

# @app.route("/years")
# def candidates():
#     """Return a list of years in the dataset"""

# @app.route("/financial_votes")
# def candidates():
#     """Return a list of all candidates financial data and election results"""