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

print(soup.prettify)

