import  os
os.chdir('/home/jp/Downloads/learn_python3/Videos')
print(os.getcwd())
for file in os.listdir():
    #print(file)
# spliting the file extension
    #print(os.path.splitdrive(file))
# retriving the file name and extension separately
    f_name , f_exte = os.path.splitext(file)  
    #print(f_name,f_exte)    

# here you can aslo spilit thw f_name oe f_extention
for file in os.listdir():
    f_name , f_exte = os.path.splitext(file) 
    f_title, f_course , f_chapter =f_name.split('-')
    #print(f_title)

    #using the strip() fun
    f_title=f_title.strip()[1:].zfill(2)  # use to fill the zero befor the digiit
    f_course=f_course.strip()
    f_chapter=f_chapter.strip()
    
    print('{}-{}-{}'.format(f_title,f_course,f_chapter))
     #Renaming the file 
    new_name= '{}-{}'.format(f_title,f_chapter)
    os.rename(file,new_name)

