
print("this method will always run ") #bcz this is outside of the main() method 
#print("the first Module's Name is {}".format(__name__))

#whenever python runs a file before  it sets a few special variable so __name__ is one of them
# so when python runs a python file dritecly so it says that __name__ variable is eqal to __main__
# so when  we import the file first_module... than the file name is set to the __name__ variable  
#that's why module for imported file will be first_Module__main__PY

def main():
    print("the first Module's Name is {}".format(__name__))
    
if __name__ == '__main__':
    main()

#above if statement is for : 
#that if the file is directly run by python or being imported  
#if statement is true than run main() method

#Comment above method and run this 

if __name__ == '__main__':
    print('Runing directly')
else:
    print('Running form import')    