
#---------------------------------------------------------------------------------------------------------------#
#                                       1. Inheritance : 
#---------------------------------------------------------------------------------------------------------------#

# It is a creating a new class which is the dreivative of the existing class
# Means from parent classa to sub or child class.
 
'''
class Parent:
    Members of the parent class

class Child(Parent):
    Inherited members from parent class
    Additional members of the child class

# Note:
python uses Method Resolution Order (MRO) that determines the flow of execution. 
MRO is a set of rules, or an algorithm, that Python uses to implement monotonicity, 
which refers to the order or sequence in which the interpreter will look for 
the variables and functions to implement. 
'''
class A:
   def __init__(self) -> None:
      print("it is init in A ")

   def func1(self):
      print("func1 is working in A")
   def func2(self):
      print("func 2 is working")

class B(A):  # B is ineriting feature of A means B is sub class and A is super or parent class

   def __init__(self) -> None:
    #  super().__init__() # It will access the all the features of the parent class , so init of A and init of B s called
      print("it is init of B")
   def func1(self):
      print("func1 is in B") # same method in A and B class so the method in the left will be priotize in the order
   def func3(self):
      print("func 3 is working")
   def func4(self):
      print("func 4 is working")

class C(B):  # C is inheriting feature of A, B so it is multilevel inherit.
   def func5(self):
      print("func 5 is working")

class D(A):  # D is ineriting feature of A
      def func6(self):
        print("func 6 is working")

class E(B,D): # Have to create this class for multilevel to avoid the MRO conflicts
   print(" Func 7 is working from class E as multilevel and avoid the MRO")
   def __init__(self) -> None: # 1st init of itself than the inti of the super is called
      super().__init__()
      # In the multilevel inherit the method is always preferd from the left to right like it will call from B first not D
   def feat(self):
      super.func1() # Method of super class
      de = B()
      


a1 =A()
b1= B()
c11= C()
d1 = D()
e1 =E()
a1=E()

a1.func1()
a1.func2() 
b1.func1() # inerited from A, Single level inheritance
b1.func3()     
c11.func1() 
c11.func5()
d1.func1()
e1.func4() # Multilevel inheritance

#---------------------------------------------------------------------------------------------------------------#
#             Constructor in inheritance : How constructor behave in inherit.
#---------------------------------------------------------------------------------------------------------------#
a1 =B() 
# the constructor is called for every function call in the class A
# When we don't have the init in the B then due to inheritance it will go to A if the relative method is called





# ----------------------------------------------Coursera Notes------------------------------------------#

#Inheritence IN Py
'''' 
object(__builtins__)  #The base class of the class hierarchy.
# objects(built -in class)
#every class in py inherits from built in base class called objcts ,
 which is found in built-ins dot objects

#like
class Aclass()
    #means
class Aclass(object)    

class types:
1. Base class/parent/super

2. child/sub/derived class

# Child class extend the behaviour  and attributes of the parents class which allows to:
1. Add more properties to child class

2. Modify inherited properties in child class

'''
#______________________________________
# Inheritence class Example: 1.
#---------------------------------------

class employee():
    def __init__(self,name,last) -> None:
        self.name=name 
        self.last =last 
class manager(employee):
    def __init__(self, name, last,position) -> None:
        super().__init__(name, last)
        self.position=position

class supervisors(employee):
    def __init__(self, name, last) -> None:
        super().__init__(name, last)
    def leave_request(self,days):
        return "You can take leave for " + str(days) +" days"   

#creating the instances for the classes 

puneetS=manager("Puneet","S","manager")

Jatav=supervisors("AJ","J")
Satav=supervisors("SS","s")

print(Jatav.leave_request(4))
print(puneetS.position)
print(Satav.name)



#------------------------
#Example 2.
#--------------------------
class Employee:  #class is the blueprint for creating the instances
   
   raise_amt = 1.04
   def __init__(self,first,last,pay): #first instance is self
        self.first =first      # this method called intialize and in other language  it called as constructer
        self.last = last
        self.pay =pay
        self.email = first + '.' + last + '@email.com'
        
   def fullname(self):
        return '{} {}'.format(self.first,self.last)
   
   def apply_raise(self):
       self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt =10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        #Employer.__init__(self,first,last,pay)
        self.prog_lang =prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay,employees =None): #None because we dont want to pass mutable data types list or dict as a argument
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees    

    def add_emp(self,emp):  #adding employee
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):  #removing employee
        if emp  in self.employees:
            self.employees.remove(emp)        
    
    def print_emp(self):
        for emp in self.employees:
            print('--->',emp.fullname())

#---------------------------------------
#Developer Class Use

#print(help(Developer))  #It will show the inheriting method of the class

dev_emp1= Developer('jp','pal',50000,'Python')
dev_emp2 = Developer('AK','last',20000,'C++')
# print(dev_emp1)

print(dev_emp1.email)
print(dev_emp1.prog_lang)

print(dev_emp1.pay)
dev_emp1.apply_raise()
print(dev_emp1.pay)

#---------------------------------------------------------------
#Manager Class use

manager_1 =Manager('Devin', 'robo', 90000,[dev_emp1]) #supervising the dev_emp1
print(manager_1.email)

manager_1.add_emp(dev_emp2)
manager_1.remove_emp(dev_emp1)

manager_1.print_emp()  #printing the full name which is spervised

#builtin functions
print(isinstance(manager_1,Employee))
print(isinstance(manager_1,Developer))
print(issubclass(Manager,Employee))
      
#-----------------------------------------------------------------


#----------------------------------------------------------------------
#Multiple Inheritance 
#---------------------------------------------------------------------

#1.____Single Inheritence________

class A():
    pass
class B(A):
    pass

#2._________Multiple Inheritence ______________

class A():
   a = 1
   
class B():
   b = 2
   
class C(A, B):
   pass

c = C()
print(c.a, c.b)

# two classes called A and B are created and then variables a and b respectively are initialized with values. 
#  A new class C is then defined and classes A and B are passed to it. 
#  This is how multiple inheritance is done in Python.

#---------------------------------------------------------
#3._______________ Multi Level Inheritance_______________

class A():
    a=1
class B(A):
    b=2
class C(B):
    pass
c = C()
print(c.a)    
print(isinstance(c,A))

# there are three level of inheritance 
# Above example of multi-level inheritance where the derived class C inherits from base class B.
# The class B is in turn a derived class of base class C. Class B here is an intermediary derived class. 
#_________________________________________________________________________________________________________

#----------------------------------------------------
# Built in Functions 
#-----------------------------------------------------

#There are two built-in functions that can come in handy when trying to find 
# the relationship between different classes and objects: issubclass() and isinstance().

issubclass(A,B)
print(issubclass(A,B)) # is A  subclass of B 
print(issubclass(C,A)) # is C subclass of A 
 

#------------------------------------------
# Super() function.
#---------------------------------------p
 #The super() function is a built-in function that can be called inside the derived class and gives access to the methods and 
#variables of the parent classes or sibling classes.
 

class Fruit():
    def __init__(self,fruit) -> None:
        print('Fruit type', fruit)

class FruitFlavour(Fruit):
    def __init__(self) -> None:
        super().__init__('apple') # changes inside the derived class
        print("Appple is sweet")

apple=FruitFlavour()
 
#This happened because when you initialize the child class, you don’t initialize the base class with it. 
#  super() function helps you to achieve this and add the initialization of base class with the derived class.




