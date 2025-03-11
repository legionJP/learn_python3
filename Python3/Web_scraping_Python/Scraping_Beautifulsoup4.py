# web Scraping in the Python using the Beautifulsoup4 

# pip install beautifulsoup4 

# pip install lxml
# pip install html5lib

# pip install requests

from bs4 import BeautifulSoup
import requests

#paasing the html file 

with open ('example.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

#print(soup.prettify()) #Parsing the whole content 

match1 = soup.title
match2 = soup.title.text
#match = soup.div #getting the first div 
#using  the find method to search for the div with class footer 
# print(match)
# print(match1)
# print(match2)

#-----------------------------------------------------------
#Scraping  the headline and the summary from example.html 

article= soup.find('div', class_ ='article') #class_ bcz , in py class is special keyword
print(article)
headline = article.h2.a.text
summary = article.p.text
print(summary)
print()
#or 

for article in soup.find_all('div',class_ ='article'):
    headline = article.h2.a.text
    print(headline)
    
    summary = article.p.text
    print(summary)
    
    print()


#---------------------------------------------------------------------------------
# Scrapping the website

#--------------------------------------------------------
    
import csv
from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.patreon.com/coreyms').text
soup = BeautifulSoup(source,'lxml')

print(soup.prettify())
print()

csv_file = open('cms_scrape.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow([headline,summary])

#---------------------------------------------------------------------------------------
# scraping the youtube video and id
#------------------------------------

# for article in soup.find_all('article'):
#     headline = article.h2.text
#     print(headline)

#     summary = article.find('div', class_ = 'entry-content').p.text
#     print(summary)

#     article = soup.find('div', class_ = 'sc-bdvvtL lhrfPG') #.p.txt
#     print(article.prettify())
 
#     try:
#         vid_src = article.find('iframe', class_ = 'youtube-player')['src'] #iframe as a attribute for the src  attribute of that tag
#         print(vid_src)    

#     #spiliting the id string 
#         vid_id = vid_src.spilit('/')
#         print(vid_id)
#      # as a list the item is hown with the index value 
#      #link at the 4 index

#         vid_id = vid_id.split('/')[4]
#         vid_id = vid_id.spilit('?')[0]# spliting based on ? 
#         print(vid_id) #video id = K6L6KVGG-7o

#         yt_link = f'https://youtube.com/watch?v={vid_id}'
#         print(yt_link)

#     except Exception as e:
#         raise e
#     print()

#     csv_writer.writerow([headline, summary, yt_link])
#     csv_file.close()









