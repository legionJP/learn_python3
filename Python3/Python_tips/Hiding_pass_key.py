#---------------------------
#Hiding Pass/Key on Windows: 
#--------------------------
import os

# db_user = 'my_db_user'
# db_password = 'my_db_pass1234!'

db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASS')

print(db_user)
print(db_password)

#--------------------------
# 2. Hiding the pass key on Linux/Mac
#----------------------------
#this is done by modifying the '.bash_profile'

#1.got to the home dir , type cd
#2.then open : nano .bash_profile
#3.export DB_USER='my_db_user'
#4.export DB_PASS='my_db_pass1234!'

db_user1 = os.environ.get('DB_USER')
db_password1 = os.environ.get('DB_PASS')
print(db_user1)
print(db_password1)