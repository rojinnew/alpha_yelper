DOC folder contains: 
(1) Final report write-up (team03report.pdf)
(2) Final poster presentation (team03poster.pdf and team03posterpresentation.mp4)

SW folder contains:
(1) Python3 script for converting dataset in JSON to CSV (convert_csv.py)
(2) Shell script for importing dataset in CSV into graph database (import.sh)
(3) Python2 script for feature engineering and graph analyses (analyze.py)
(4) Python2 script for generating data for GUI (gui.py)
(5) AlphaSelects folder - GUI related files

Installation and Setup: (please email contact person - angkul@gatech.edu - if an assistance is needed)
(1) Download a dataset from Yelp Dataset Challenge at https://www.yelp.com/dataset_challenge/dataset/
(2) Extract Yelp dataset in SW folder using tar command with xzvf options
(3) Run JSON to CSV conversion python script (python3 convert_csv.py)
(4) Download Neo4j Community Edition from http://neo4j.com/download/
(5) Extract Neo4j in SW folder using tar command with xzvf options
(6) Edit neo4j-server.properties file in conf folder inside an extracted Neo4j folder to disable the requirement of authentication to access Neo4j by changing dbms.security.auth_enabled=true to false
(7) Run import script (./import.sh) in SW folder to create a graph database from CSV files of Yelp dataset from step (3) - you may need to install realpath
(8) Start Neo4j server (./neo4j start) in bin folder inside an extracted Neo4j folder

To run a demo for data analyses:
(9) Run python script for feature engineering and graph analyses (python analyze.py) - this step takes about 15 minutes on our platform - you may need to install a few python packages

To run a demo for GUI:
(10) Run python script to generate data for GUI (python gui.py)
(11) Start web server in the AlphaSelects folder inside SW folder (python -m SimpleHTTPServer)
(12) Open a web browser, maximize it, and view GUI at localhost:8000 (tested in chrome on Ubuntu)
