import sqlite3

#connect to database
#if database doesn't exist, create database
conn = sqlite3.connect('dict.db')

#create a cursor
cursor = conn.cursor()

##create table
#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

print(cursor.rowcount)

##insert record
#cursor.execute('insert into user(id, name) values (\'1\', \'Eduard\')')

print(cursor.rowcount)

values = cursor.fetchall()

#close cursor
cursor.close()

#commit
conn.commit()

#close connection
conn.close()


for v in values:
    print(v)
