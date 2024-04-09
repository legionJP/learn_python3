from employee import Employee ,Manager

import sqlite3

emp1= Employee('Amar','dubey',54323)
emp2= Employee('sachit','hola',675894)
print(emp1.pay)

#making the connection object

#making the in-memory database for tempary based, it live in ram and refresh every time when we run 
db_conn =sqlite3.connect(':memory:') 

#for filename db, for stroing the db in file 
#db_conn = sqlite3.connect('employee.db')

c= db_conn.cursor()   #creating the cursor for excexuting sql command

#adding the data in db table 

# c.execute("""CREATE TABLE employees(
#           first text,
#           last text,
#           pay integer
# )""")


c.execute("INSERT INTO employees VALUES ('Akash','Kumar',45435)")

#using the string formating , but this is vurneable for sql injection
# c.execute("INSERT INTO employees VALUES('{}','{}','{}'".format(emp1.first,emp1.last,emp1.pay))
# db_conn.commit()

# #Using the DB API place holder (?) and putting the value in tuple form 
c.execute("INSERT INTO employees VALUES(?,?,?)",(emp1.first, emp1.last, emp1.pay))
db_conn.commit()

# or using the : and name of place holder , here we use dictionary instead of tuple , key will be place holder name and value will be what data we want to insert
c.execute("INSERT INTO employees VALUES(:first , :last , :pay)"
          ,{'first':emp2.first,'last':emp2.last, 'pay':emp2.pay})
db_conn.commit()

c.execute("SELECT * FROM employees where last ='Kumar'")
print(c.fetchone()) #only returne one

c.execute("SELECT * FROM employees where last =?",('hola',)) #this one is haaving the tuple value so use ,
print(c.fetchall())

c.execute("SELECT * FROM employees where last =:last",{'last': 'dubey'}) #this one is in dictionary
print(c.fetchall())


# c.fetchmany(5) #number of  rows as a lis
# c.fetchmany() 

db_conn.commit() #commiting the changes

db_conn.close()
