## Log Analysis - reporting tool

This project generates a report querying a mock PostgreSQL database for a fictional news website. The project involves creating a reporting tool using Python program. The Python code uses the `psycopg2` module to connect to the database and query the data for following:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors? 

### Installation

1. Download [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)  to install virtual machine. 
2. Use the below commands to bring the virtual machine online and to login respectively:
	`vagrant up` - which will take several minutes and returns the terminal prompt on success
	`vagrant ssh` - used for logging in to VM
3. Download the news data provided by Udacity [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Unzip the file and place newsdata.sql inside the Vagrant folder.
4. Load the database using the command `psql -d news -f newsdata.sql`
5. Connect to the database using the command `psql -d news`
6. You may query the db to verify the data
7. Once done, exit psql.

### Execution

Now execute the Python file using the command `python logAnalysis.py`
