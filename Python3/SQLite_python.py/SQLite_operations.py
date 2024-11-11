import sqlite3  
from employee import Employee
#-----------------------------
#making the connection object
#-----------------------------

#making the in-memory database for tempary based, it live in ram and refresh every time when we run 
db_conn =sqlite3.connect(':memory:') 

#for filename db, for stroing the db in file 
#db_conn = sqlite3.connect('employee.db')

c= db_conn.cursor()   #creating the cursor for excexuting sql command

#---------------------------
#adding the data in db table 
#-----------------------------

c.execute("""CREATE TABLE employees(
          first text,
          last text,
          pay integer
)""")

def insert_emp(emp):
    with db_conn:  #using the context manager , no need to use the commit()
        c.execute("INSERT INTO employees VALUES(:first , :last , :pay)"
          ,{'first':emp.first,'last':emp.last, 'pay':emp.pay})
    
def get_by_last_name(lastname):
    c.execute("SELECT * FROM employees WHERE last =:last",{'last':lastname})
    return c.fetchall()
    
def update_pay(emp,pay):
    with db_conn:
        c.execute("""UPDATE employees SET pay = :pay WHERE first= :first AND last = :last"""
                  ,{'first':emp.first,'last':emp.last,'pay':pay})

def remove_emp(emp):
    with db_conn:
        c.execute("""DELETE from employees WHERE first =:first AND last= :last"""
                  ,{'first':emp.first,'last': emp.last})

#Insert the emp in the db 

emp11= Employee('Amar','dubey',54323)
emp2= Employee('anna','hola',675894)

insert_emp(emp11)
insert_emp(emp2)

emp_last=get_by_last_name('dubey')
print(emp_last)

update_pay(emp2,67000) 
remove_emp(emp11)

emp_last=get_by_last_name('hola')
print(emp_last)

db_conn.close()