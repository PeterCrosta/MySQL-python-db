# MySQL-python-db

I created this MySQL database to explore MySQL and the MySQL Connector. The following instructions assume that you have already installed Python3, MySQL, and MySQL terminal.

After cloning the repository, set up a virtual environment. In the terminal, type, "python3 -m venv env". Do not include my quotation marks unless I say to do so.

Select an interpreter by opening the command palette (shift, command, P), and type "Python: Select Interpreter". Select the venv option. It should start with something like, ".\env".

In the command palette, type, "Terminal: Create New Integrated Terminal. This will create a terminal for the virtual environment.

Install flask and MySQL in your virtual environment with "pip3 install flask" and "pip3 install mysql-connector-python" respectively.

Set up the database:

Go to config.ini file, update the password for your machine

Log in to your MySQL server with "mysql -u root -p". You will then be asked to enter your password.

In the MySQL command line that is now open, one line at a time, enter:
create database epilepsy_db;
use epilepsy_db;
source #the route to the epilepsy_db.sql file. (I went to its directory, used pwd, and copy/pasted it with the file name.)
SHOW TABLES;

You should see the tables, patients, regimens, and drugs.

Now, you should be able to run the program with 

To run the app, in the terminal, type "python3 -m flask run"

