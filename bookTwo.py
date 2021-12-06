# today we will get all content of the page and them we will find the elemnt from the content  
# gettext() loop() and the findAll()  functions fron the urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
#  prinat out the text that will meat  the id 
html=urlopen("https://cp-algorithms.com/")
doo=BeautifulSoup(html, "html.parser")
nameList=doo.find_all(id="container")
for name in nameList:
    print(name) 
    
    # we can also find elemts by span or HTML tage or by the keey words
    # ,find_all(["h1",'h2'])  similarly more
    
    # if we wnat the all images source in the page the we will find the images 

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#  print out the text that will tell us the detail of the image and thrie source
html=urlopen("https://unsplash.com/")
doo=BeautifulSoup(html, "html.parser")
imaes=doo.find_all("figure")
for img in imaes:
    print( "\n\n", {img})
    


#  print out the text that will tell us stringis or not
html=urlopen("https://unsplash.com/")
doo=BeautifulSoup(html, "html.parser")
imaes=doo.find_all("",text='may be he is sleeping ')
print(imaes)    
    