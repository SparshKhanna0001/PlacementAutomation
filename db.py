"""
All database function will be stored here

Functions - to get the db from appscript.gs
            to store the db at appscript.g

            then fucntions to actually add data corresponding to a companny name

            
THE STRCUTURE OF THE FILE SHUD BE SUCH THAT ALWAYS THE con object is closed.
"""


import globals
import sqlite3

PATH = globals.DB




con = sqlite3.connect(PATH)         
#con = sqlite3.connect('data.db')
cur = con.cursor()


#shud be executed when the porgram is ran the first time
def create():

    company = """CREATE TABLE COMPANY_(company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL UNIQUE,
    address TEXT NOT NULL,
    services_offered TEXT,
    revenue VARCHAR(50), 
    employees INTEGER)"""
   
    person = """CREATE TABLE PERSON_DETAILS (individual_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15),
    email VARCHAR(100),
    company_id INTEGER NOT NULL,
    position VARCHAR(100),
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE)"""

    cur.execute(company)
    cur.execute(person)

