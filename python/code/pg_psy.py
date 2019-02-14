#!/usr/bin/python
import psycopg2
import sys
db_con = None
try:
#Create a database session
    db_con = psycopg2.connect(database='latihan', user='postgres', password='mirotakampus',host='127.0.0.1', port='5432')
#Create a client cursor to execute commands
    cursor = db_con.cursor()
    cursor.execute("create table customers (id serial primary key, name varchar, age integer);")
#The variables placeholder must always be a %s, psycop2 will automatically convert the values to SQL literal
    cursor.execute("insert into customers ( name, age) values(%s,%s)", ("leo", 26))
    db_con.commit()
    cursor.execute("select * from customers")
    print(cursor.fetchone())
except psycopg2.DatabaseError as e:
    print ('Error %s' % e )
    sys.exit(1)
finally:
    if db_con:
        db_con.close()
