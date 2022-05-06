import psycopg2
from config import database

conn = psycopg2.connect(**database)
cursor = conn.cursor()

sql_code = """CREATE TABLE Phone(
	NAME VARCHAR ( 255 ) NOT NULL,
	PHONENUMBER VARCHAR ( 255 ) NOT NULL
);
"""

cursor.execute(sql_code)
conn.commit()
