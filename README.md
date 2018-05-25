# Logs Analysis Project

> Omar Piñero Rivera

## About

This is a project for the Full Stack Web Developer Nanodegree from Udacity. This project consist to build an internal reporting tool from an articles site database to answer questions about users activities. 

The database contains an articles, authors and log tables. The report should be able connect to the database and perform the required sql queries to answer the following questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time? 
3. On which days did more than 1% of requests lead to errors?  

## To Run

### You will need:
- Python3
- Vagrant
- VirtualBox
- Download the Data newsdata.sql file from Udacity

### Setup
1. Install Vagrant And VirtualBox
2. Clone this repository
3. Move the newsdata.sql file inside the vagrant folder

### To Run

Launch Vagrant VM by running `vagrant up`, then run the secure shell command `vagrant ssh` and then type `cd /vagrant` to access the shared files.

To create the tables and load the data, use the command `psql -d news -f newsdata.sql`. Then run the command `psql -d news -f logs_analysis_views.sql` to create the required views to run the python program. 

_The following database tables and views should be created:_

> - authors table
> - articles table
> - log table
> - total_group view
> - errors_group view
> - errors_rate_group view

Finally to execute the program, run `python logs_analysis_project.py` from the command line.
