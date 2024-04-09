import sqlite3

#making the connection object

conn =sqlite3.connect(':memory:') #making the in-memory database


#for filename db
db_conn = sqlite3.connect('employee.db')

c= db_conn.cursor()   #creating the cursor for excexuting sql command

# c.execute("""CREATE TABLE employees(
#           first text,
#           last text,
#           pay integer
# )""")

#adding the data in db table 

# c.execute("INSERT INTO employees VALUES ('Akash','Kumar',45435)")

c.execute("SELECT * FROM employees where last ='Kumar'")
c.fetchone() #only returne one

# c.fetchmany(5) #number of  rows as a lis
# c.fetchmany() 

db_conn.commit() #commiting the changes

db_conn.close()