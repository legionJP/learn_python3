import csv

# # Reading the CSV file 
'''
with open('names.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    #next(csv_reader)      #by using the generator for next item iteration
     
# for line in csv_reader:
#       #print(line)
#        print(line[2])

# Writing the new csv file from previous one with delimiter

    with open('new_names.csv','w') as new_file:
        csv_writer = csv.writer(new_file,delimiter='-')
    
        for line in csv_reader:
            csv_writer.writerow(line)
'''
'''
with open('names.csv', 'r') as csv_file1:
    csv_reader1 =csv.DictReader(csv_file1) # it prints/read the csv in key value pair 

    for line  in csv_reader1:
        #print(line)
        print(line['email']) # csn print the value by key 
'''
# DictWriter Method

with open ('names.csv','r') as csv_file2:
    csv_reader2 = csv.DictReader(csv_file2)

    with open('new_names.csv','w') as new_file1:
        fieldnames = ['first_name', 'last_name', 'email']
        #fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_file1, fieldnames=fieldnames,delimiter='\t')

        csv_writer.writeheader()

        for line in  csv_reader2:
            #del line['email']
            csv_writer.writerow(line)   
            print(line)    
