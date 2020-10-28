# Election Web App - Flask

**Repo Link:**  https://github.com/jrhoads1004/ETL_project

**Install a web app to Investigate Presidential Election Data**  
* search by a certain year from years 2000-2016

**Setup**
* Download pgAdmin - https://www.pgadmin.org/download/
* Create Database in pgAdmin
* Right click on your created Database and select query tool
* Add the code from (election_db_sql.sql) to create the tables to the database 
* Make sure pgAdmin is still open and run the following command - python app.py
* go to your web browser and type in localhost:5000/
* localhost:5000/summary will give you the complete list
* if you want to select a certain year then type - localhost:5000/results/yyyy 

**Possible investigation that could be done with the final database:**
* Campaign Fund data and Presidential Election data can be combined to determine:
* Does raising more funds lead to a candidate’s election?
* Which presidential candidate has more/less debt?

**Final Database:**  Relational database due to the relationship between the presidential candidate column between the two datasets
