#--------------------------------------------------------------------------------------------#
#                             Thredas:  
#--------------------------------------------------------------------------------------------#

'''
small unit  of process a single sequence of instructions that can be managed independently
 by the operating system. Multiple threads can exist within a single process,
 sharing the same resources like memory and file handles.
'''
#--------------------------------------------------------------------------------------------#
# Multithreading

'''Multithreading is a programming technique where multiple threads are used within 
a single process to perform tasks concurrently.
This can improve the performance of applications, especially for tasks
that involve I/O operations, like reading from a file or making network requests.
'''

#--------------------------------------------------------------------------------------------#
from threading import *
import threading
from time import sleep 

class hello(Thread):           # After putting the thread in the class they will run indivitually with different thread

    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)


class hi(Thread):
    def run(self):   # there is inbuilt method for the run in the thread class so run is use for executing with start
        for i in range(5):
            print("Hi")
            sleep(1)    

# h1 = hello()
# h2= hi()  

# # h1.run()
# # h2.run()
# h1.start()
# sleep(0.2) # delay the execution to stop the colliasion
# h2.start()
# #print("bye")  # here the Main thread is printing not depended on the h1 and h2

# h1.join()  # This will wait to the h1 and h2 thred to complete then print the main thread Bye
# h2.join()
# print("Bye")

# All the code is using the 1 core when the Thread class is not passed ..

# To Execute the h1 and h2 simultaneously use the Thread class
# Above executin is done by the one thread

#-------------------------------------------------------------------------------------------------------------#

# Creating threads: Method 2 without using the run method in the class
def print_numbers():
    for i in range(5):
        print(i)
        sleep(1)

def print_letters():
    for i in "ABCDE":
        print(i)
        sleep(1)

thread1 = threading.Thread(target=print_numbers) 
thread2 = threading.Thread(target=print_letters)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Thread 1 and 2 running the simultaneously")

#-------------------------------------------------------------------------------------------------------------#
