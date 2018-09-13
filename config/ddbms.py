#!/usr/bin/python
import psycopg2

hostname = '35.187.38.114'
username = 'lexxinet_admin'
password = 'password'
database = 'lexxinet'
port = 5432


# Simple routine to run a query on a database and print the results:
def doQuery(conn):
    cur = conn.cursor()

    cur.execute("SELECT DISTINCT first_name, last_name FROM users_user WHERE last_name LIKE 'Mwangi'")

    for first_name, last_name in cur.fetchall():
        print first_name, last_name


myConnection = psycopg2.connect(host=hostname, port=port, user=username, password=password, dbname=database)
doQuery(myConnection)
myConnection.close()
