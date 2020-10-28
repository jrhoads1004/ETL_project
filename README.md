# Election Web App - Flask

**Repo Link:**  https://github.com/jrhoads1004/ETL_project

**Group 16:**  Nick Orewiler, Christy Patrick, Josh Rhoads

## Introduction
This project uses ETL on presidential candidate data from the years 2000 – 2016.  

**Use Cases and possible investigation that could be done with the final database:**
* Is there a relationship between the amount of funds raised by a presidential candidate and whether they win the election? Does raising more funds lead to a candidate’s election?
* Is there a relationship between the amount of funds spent by a presidential candidate and whether they win the election? Does spending more funds lead to a candidate’s election?
* Which presidential candidate has more or less debt for each election?  Does this have an impact on the election results?

## Data Sources
**Presidential Candidate Financial Data**
* Type:  OpenFEC API
* Financial Reporting using the /elections/ endpoints
* URL - https://api.open.fec.gov/developers/#/financial/get_elections_

**Presidential Candidate Election Data**
* Type:  CSV
* Federal Election Publications
* URL - https://www.fec.gov/introduction-campaign-finance/election-and-voting-information/

## Extract, Transform, Load 

### Extract (E)
* API – Candidate Financial Data
  * Created API Key
  * Used the /elections/ endpoint
  * Tested API for 1 election year in Jupyter Notebook
  * Finally, looped through election years to get presidential election data for 2000-2016 into a single DataFrame in Jupyter Notebook

* CSV – Candidate Election Data
  * Data was embedded in a publication file; extracted table of interest into csv
  * Single file for each election year between 2000-2016
  * Merged the individual files into a single DataFrame in Jupyter Notebook

### Transform (T)
* Candidate Financial Data:
  *  candidate names 
    * Name column to display “first name last name”
    * Removed vice president candidate names
    * Removed “/” and “.”
    * Removed middle names (like Rodham)
    * Removed extra spaces

* Candidate Election Data:
  * Removed extra data from the candidate name column (such as party, platform, etc)
  * Removed the following: “,”   “.”   ”%”
  * Lowercase all column names
  * Removed 

* Both tables:
  * Added key column to both tables by combining the candidate name column + election year column to be used to join both tables in the database

### Load (L)
* **Database Type:** SQL – Relational <br>
* **Why SQL?**  The tables in the database are related in that they both contain presidential candidate information by year.  The two tables are joined by a key referencing their name and election year.

* Load Steps:
  * Created tables and scheme in Postgres (PgAdmin)
  * In Jupyter Notebook:
    * Connected to the database
    * Verified tables existed
    * Used Pandas to load the DataFrames into Database
    * Confirmed data loaded into the tables by querying
  * In Postgres:
    * Queried the db to verify that it loaded
    * Joined the tables to verify data and key alignment

## Schema of the tables
**Table 1 - candidate_financial**
* key VARCHAR(100) PRIMARY KEY
* candidate_election_year VARCHAR(4)
* candidate_id VARCHAR(50)
* candidate_name VARCHAR(10)
* party_full VARCHAR(50)
* total_receipts DECIMAL
* total_disbursements DECIMAL
* cash_on_hand_end_period DECIMAL

**Table 2 - candidate_votes**
 * key VARCHAR(100) PRIMARY KEY
  * key VARCHAR(100) PRIMARY KEY
  * name VARCHAR(100)
  * votes INT
  * votepct DECIMAL
  * year VARCHAR(4)

## Flask Application

### Summary Route:
![summary_route](https://github.com/jrhoads1004/ETL_project/blob/main/images/Flask%20Summary%20Route.png)

### Variable Year Route (year 2000 is displayed below):
![year_route](https://github.com/jrhoads1004/ETL_project/blob/main/images/Flask%20Year%20Route.png)

### To use the Flask Application, use the steps provided below:

**Install a web app to Investigate Presidential Election Data**  
* search by a certain year from years 2000-2016

**Setup**
* Download pgAdmin - https://www.pgadmin.org/download/
* Create Database in pgAdmin
* Run schema file to create the tables - (election_db_sql.sql)
* Open jupyter notebook under your ETL_project directory and run - MainNotebook.ipynb
* Make sure pgAdmin is still open and run the following command - python app.py
* Go to your web browser and type in localhost:5000/
* localhost:5000/summary will give you the complete list
* If you want to select a certain year then type - localhost:5000/results/yyyy 
