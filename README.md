### Summary
<p align="justify"> 
This project presents a novel method for discovering influential reviewers on online review websites. The proposed method relies on temporal correlations of reviews from a cluster of social network groups. These correlations are represented as graphs and the analyses are carried out through queries on graph database. For evaluation, the proposed method was applied to the dataset from Yelp Dataset Challenge, which includes 500K+ reviewers (a.k.a. yelpers), 75K+ businesses, and 2M+ reviews, yielding 12K+ trendsetting reviewers with drastically different levels of influences on Yelp. The PageRank algorithm then ranks these trendsetters with top ten ranks chosen as alphas. The evaluation results from assessing the accuracy of business rating prediction by these alphas are shown to be superior to that of the elite yelpers. The graphical user interface for utilizing the alpha’s capabilities also demonstrated that rating and review from alpha yelpers can be used to reduce the length of time for locating good businesses.
<p align="justify">

![Image](https://github.com/rojinnew/alpha_yelper/blob/master/image.png)

#### DOC folder contains: 

(1) Final write-up (team03)

#### SW folder contains

(1) Python3 script for converting dataset in JSON to CSV (convert_csv.py)

(2) Shell script for importing dataset in CSV into graph database (import.sh)

(3) Python2 script for feature engineering and graph analyses (analyze.py)

(4) Python2 script for generating data for GUI (gui.py)

(5) AlphaSelects folder - GUI related files

#### Installation and Setup 

(1) Download a dataset from Yelp Dataset Challenge at https://www.yelp.com/dataset_challenge/dataset/

(2) Extract Yelp dataset in SW folder using tar command with xzvf options

(3) Run JSON to CSV conversion python script (python3 convert_csv.py)

(4) Download Neo4j Community Edition from http://neo4j.com/download/

(5) Extract Neo4j in SW folder using tar command with xzvf options

(6) Edit neo4j-server.properties file in conf folder inside an extracted Neo4j folder to disable the requirement of authentication to access Neo4j by changing dbms.security.auth_enabled=true to false

(7) Run import script (./import.sh) in SW folder to create a graph database from CSV files of Yelp dataset from step (3) - you may need to install realpath

(8) Start Neo4j server (./neo4j start) in bin folder inside an extracted Neo4j folder

#### To run a demo for data analyses

(9) Run python script for feature engineering and graph analyses (python analyze.py) - this step takes about 15 minutes on our platform - you may need to install a few python packages

#### To run a demo for GUI

(10) Run python script to generate data for GUI (python gui.py)

(11) Start web server in the AlphaSelects folder inside SW folder (python -m SimpleHTTPServer)

(12) Open a web browser, maximize it, and view GUI at localhost:8000 (tested in chrome on Ubuntu)
