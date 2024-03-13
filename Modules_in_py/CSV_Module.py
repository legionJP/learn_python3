import csv
with open('names.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    #next(csv_reader)      #by using the generator for next item iteration
    '''for line in csv_reader:
        #print(line)
        print(line[2])'''
    with open('new_names.csv','w') as new_file:
        csv_writer = csv.writer(new_file,delimiter='-')
    
        for line in csv_reader:
            csv_writer.writerow(line)