import Python3.Modules_in_py.Modules_Intro.first_module__main__PY as first_module__main__PY
#py is importing the file and so module is the file name 
#when we have if statement in the first_module file it is not printing the imported module name

#to run main method in second module, can use this code
first_module__main__PY.main()

print('second Module name is {}'.format(__name__))
# second module is __main__ , because the python is runnig the file directly
