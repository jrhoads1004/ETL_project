CREATE TABLE IF NOT EXISTS candidate_financial(
	key VARCHAR(100) PRIMARY KEY,
	candidate_election_year VARCHAR(4), 
	candidate_id VARCHAR(50), 
	candidate_name VARCHAR(100),
	party_full VARCHAR(50), 
	total_receipts DECIMAL, 
	total_disbursements DECIMAL, 
	cash_on_hand_end_period DECIMAL
);



CREATE TABLE IF NOT EXISTS candidate_votes(
	key VARCHAR(100) PRIMARY KEY,
	name VARCHAR(100), 
	votes INT, 
	votepct DECIMAL, 
	year VARCHAR(4)
);

select * from candidate_votes;

select * from candidate_financial;

SELECT
f.candidate_election_year, f.candidate_name, f.party_full, f.total_receipts, f.total_disbursements, f.cash_on_hand_end_period, 
v.votes, v.votepct
FROM candidate_financial f
JOIN candidate_votes v
	ON f.key=v.key;
