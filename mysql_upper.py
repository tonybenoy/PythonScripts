# -*- coding: utf-8 -*-
__author__ = "Tony Benoy"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "me@tonybenoy.com"
import MySQLdb
#Enter host here
host=""
#Enter user here
user=""
#Enter password here
passwd=""
#Enter database name here
database=""
#Enter table name here here
table_name="''"
db = MySQLdb.connect(host, user, passwd, database)
cursormysql = db.cursor()
sql = "SELECT COLUMN_NAME FROM information_schema. columns WHERE table_name = "+table_name 
cursormysql.execute(sql)
row =cursormysql.fetchall()
name=[]
new_name=[]
for a in row:
    print a
    name.append(str(a[0]))
sql ="SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = "+table_name
cursormysql.execute()
row =cursormysql.fetchall()
typec=[]
for a in row:
     typec.append(str(a[0]))
for t in range(0,len(name)):
    print sql
    sql ='ALTER TABLE '+table_name+'change '+name[t]+' '+name[t].lower()+' ' +typec[t]
    cursormysql.execute(sql)
db.commit()
db.close()

