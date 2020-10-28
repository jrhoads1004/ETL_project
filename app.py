import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, and_

from flask import Flask, jsonify


#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


#################################################
# Database Setup
#################################################

# Create engine
pg_user = 'postgres'
pg_password = 'NextStory86@'
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

@app.route("/")
def home():
    return (
        f"HOME PAGE</br>"
        f"==== Available Routes ====<br/>"
        f"/summary<br/>"
        f"/results/yyyy"
    )

@app.route("/summary")
def summary():
    """Return a list of candidates that have ran for president"""
    session = Session(engine)

    results = session.query(Candidate_Votes, Candidate_Financial).filter(Candidate_Votes.key == Candidate_Financial.key).all()

    # close the session to end the communication with the database
    session.close()

    # Convert the query results to a dictionary
    summary_list = []
    for v, f in results:
        summary_dict = {}
        summary_dict["election_year"] = f.candidate_election_year
        summary_dict["name"] = f.candidate_name
        summary_dict["party_full"] = f.party_full
        summary_dict["total_receipts"] = str(f.total_receipts)
        summary_dict["total_disbursements"] = str(f.total_disbursements)
        summary_dict["cash_on_hand_end_period"] = str(f.cash_on_hand_end_period)
        summary_dict["votes"] = str(v.votes)
        summary_dict["votepct"] = str(v.votepct)
        summary_list.append(summary_dict)

    # Return the JSON representation of the dictionary
    return jsonify(summary_list)


@app.route("/results/<given_year>")
def yr_results(given_year):
    """Return a list of candidates that have ran for president"""
    session = Session(engine)

    results = session.query(Candidate_Votes, Candidate_Financial).filter(and_(Candidate_Votes.key == Candidate_Financial.key, Candidate_Votes.year == given_year)).all()

    # close the session to end the communication with the database
    session.close()

    # Convert the query results to a dictionary
    summary_list = []
    for v, f in results:
        summary_dict = {}
        summary_dict["name"] = v.name
        summary_dict["party_full"] = f.party_full
        summary_dict["total_receipts"] = str(f.total_receipts)
        summary_dict["total_disbursements"] = str(f.total_disbursements)
        summary_dict["votes"] = str(v.votes)
        summary_dict["votepct"] = str(v.votepct)

        summary_list.append(summary_dict)

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