# we will track all the Links and a tages in a page that will be routed
#  find all Links from a pages 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# Print out all route to the Link Page these are two websites
html=urlopen("https://cp-algorithms.com/" and "https://the-algorithms.com/")
one=BeautifulSoup(html,"html.parser")
for link in one.find("div",{"id":"bodyContent"}).find_all(
    "a",href=re.compile('^(/wiki/)((?!:).)*$')):
    if "href" in link.attrs:
        print(link.attrs["href"])
        

#  find all Links from a website

# Print out all route to the Link Page these are two websites
html=urlopen("https://cp-algorithms.com/")
one=BeautifulSoup(html,"html.parser")
for link in one.find_all("a"):
    if "href" in link.attrs:
        print(link.attrs["href"])        
        
        

# add all link of the website to the file
from urllib.request import urlopen
from bs4 import BeautifulSoup


glob=[]
html=urlopen("https://cp-algorithms.com/")
one=BeautifulSoup(html,"html.parser")
for link in one.find_all("a"):
    if "href" in link.attrs:
        print(link.attrs["href"])
        glob.append(str(link.attrs["href"]))
                

# add data to the file

f=open("cpALgo.txt", "w+")
for i in glob:
    f.write(f" {i} \n")        
        
        #end 
        
# get all articles of the page and Linux

from urllib.request import urlopen 
from bs4 import BeautifulSoup 
import re

html = urlopen('http://en.wikipedia.org/wiki/linux')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find('div', {'id':'bodyContent'}).find_all(
    'a', href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])
        
        
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
# main function
random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
# get all links of the article
links = getLinks('/wiki/linux')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)        
                
                
# crawl all website 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')): #find out all the new Link of the site 
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks('')


                