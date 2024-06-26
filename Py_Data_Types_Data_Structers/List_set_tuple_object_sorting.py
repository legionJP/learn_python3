num_list=[2,36,4,15,62,74,28,19,11]
sorted_list=sorted(num_list) #sort(num_list) will retrun the nun value
print(sorted_list) # it will be the new sorted list but not the original one

#sorting the original list

num_list.sort()
#
num_list.sort(reverse=True)
print('Origina sorted list:\t', num_list)

#SORTING THE TUPLE

tup =(2,36,4,15,62,74,28,19,11)
sorted_tup =sorted(tup)  #in a case of the tuple we can't use the .sort() bcz its unmutable
print('Tuple\t',sorted_tup)

#SORTING THE Dict

di ={'name': 'jp', 'job': 'programming', 'age': None, 'os': 'Linux'}
sorted_dict=sorted(di)
print('Dict\t',sorted_dict) #its only print the key 
 
 #sorting the value based on absolute value

li =[-7,-4,-2,1,2,3]
#s_li=sorted(li)
s_li=sorted(li,key=abs)
print(s_li)

#-----------------------------------------------
#Sorting the list based on key
from operator import attrgetter
class Employee():
    def __init__(self,name ,age,salary):
        
        self.name =name
        self.age =age
        self.salary=salary

def __repr__(self):
    return '({},{},${})'.format(self.name,self.age,self.salary)

e1 = Employee('carl',37,70000)
e2 =Employee('jay',34,80000)
e3=Employee('dack',56,90000)
employees=[e1,e2,e3]
#sort_employee = sorted(emloyee) # it will give the employee object error 
#def e_sort(emp):
 #   return emp.name

#sort_employees =sorted(employees, key =e_sort,reverse=True)
#sort_employees=sorted(employees, key= lambda e: e.name)
sort_employees=sorted(employees, key= attrgetter('name'))  
print(sort_employees) #printing the only object address
