import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, and_

from flask import Flask, jsonify


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Database Setup
#################################################

# Create engine
pg_user = 'postgres'
pg_password = '****'
db_name = 'election_db'

connection_string = f"{pg_user}:{pg_password}@localhost:5432/{db_name}"
engine = create_engine(f'postgresql://{connection_string}')

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

# Save reference to the table
Candidate_Financial = Base.classes.candidate_financial
Candidate_Votes = Base.classes.candidate_votes

#################################################
# Flask Routes
#################################################

@app.route("/summary")
def summary():
    """Return a list of all candidates financial data and election results for that year"""

    # Open a communication session with the database
    session = Session(engine)

    results = session.query(Candidate_Financial.candidate_election_year, Candidate_Financial.candidate_name, Candidate_Financial.party_full,  Candidate_Financial.total_receipts, Candidate_Financial.total_disbursements, Candidate_Financial.cash_on_hand_end_period).\
            order_by(Candidate_Financial.candidate_election_year).all()
    
    # Convert the query results to a dictionary 
    summary_list = []
    for candidate in results:
        summary_dict = {}
        summary_dict["election_year"] = Candidate_Financial.candidate_election_year
        summary_dict["name"] = Candidate_Financial.candidate_name
        summary_dict["party_full"] = Candidate_Financial.party_full
        summary_dict["total_receipts"] = Candidate_Financial.total_receipts
        summary_dict["total_disbursements"] = Candidate_Financial.total_disbursements
        summary_dict["cash_on_hand_end_period"] = Candidate_Financial.cash_on_hand_end_period
        summary_list.append(summary_dict)

    # close the session to end the communication with the database
    session.close()

    # Return the JSON representation of the dictionary
    return jsonify(summary_list)

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