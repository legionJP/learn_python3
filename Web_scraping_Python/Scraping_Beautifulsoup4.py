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

####################################################################################

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

from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.webscraper.io/test-sites/e-commerce/allinone').text
soup = BeautifulSoup(source,'lxml')

print(soup.prettify())
print()

content= soup.find('div', class_ ='jumbotron')
#print(content.prettify())

summary =content.find(class_ = 'lead')


print(summary)

#---------------------------------------------------------------------------------------
# scraping the youtube video and id
for article in soup.find_all('article'):
headline = article.h2.atext
print(headline)
vid_src = article.find('iframe', class_ ='youtube-player')['src']
print(vid_src) #link of video 

vid_id = vid_src.split('/')[4]
vid_id =vid_id.split('?'[0]) # id on the 0 index of the string
print(vid_id) # SPLIT THE ID Of the video after 4 spilit

yt_link = f'https://youtube.com/watch?v ={vid_id}'
print(yt_link)





