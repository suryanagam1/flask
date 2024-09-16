from flask import Flask

import psycopg2

conn = psycopg2.connect(database="postgres",host="localhost",user="postgres",password="123456",port="5432")

cur = conn.cursor()

cur.execute('''CREATE TABLE  IF NOT EXISTS Data(id serial PRIMARY KEY,datasets varchar(100),category varchar(50),free varchar(50),rating integer,description varchar(150));''')
cur.execute('''INSERT INTO Data (datasets,category,free,rating,description) VALUES ('finance','text','Y',4,'This is Finance Dataset')
,('Analytical','image','Y',3,'This is Anlytical  Dataset'),('Health','text','N',3,'This is Health Dataset'),('Stastical','video','N',2,'This is Statistical Dataset');''')




conn.commit()
cur.close()
conn.close()
 