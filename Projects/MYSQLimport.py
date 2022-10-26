import pandas as pd
import mysql.connector as mysql
from mysql.connector import Error

empdata = pd.read_csv('domain.csv', index_col=False, delimiter=',')
empdata = empdata.fillna(0)
empdata.head()

try:
	conn = mysql.connect(host='localhost', user='test', password='test')
	if conn.is_connected():
			cursor = conn.cursor()
			cursor.execute("CREATE DATABASE domain")
			print("Database is created")
except Error as e:
		print("Error while connecting to MYSQL", e)


try:
	conn = mysql.connect(host='localhost', database = 'domain', user='test',password='test')
	if conn.is_connected():
		cursor = conn.cursor()
		cursor.execute("select database();")
		record = cursor.fetchone()
		print("You're connected to database: ", record)
		cursor.execute('DROP TABLE IF EXISTS domain_data;')
		print('Creating... table')
		cursor.execute("CREATE TABLE domain_data(subdomain varchar(255), timestamp varchar(255))")
		print("Table is created....")

		for i,row in empdata.iterrows():
			sql = "INSERT INTO feedback.feedback_data VALUES (%s, %s)"
			print(tuple(row))
			cursor.execute(sql, tuple(row))
			print("Record Inserted")
			conn.commit()
except Error as e:
	print("Error while connecting to MYSQL", e)
