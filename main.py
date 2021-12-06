# we will read the Data that we are getting from a file in differnt form in Binary or x86 form and structure them in differbnt forms

from bs4 import BeautifulSoup
# go to the urL AND GET dATA fromthe page and we will read it only 
from urllib.request import urlopen
textPage = urlopen('http://www.pythonscraping.com/pages/warandpeace/chapter1.txt')
print(textPage.read())


from urllib.request import urlopen
textPage = urlopen(
             'http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt')
#  if we get data in Binary form 
# print(textPage.read()) 
print(str(textPage.read(), 'utf-8')) #in plane tetx




# find out the dive whose id mathes and show the text
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bs = BeautifulSoup(html, "html.parser")
content = bs.find("div",{"id":"mw-content-text"}).get_text()
content = bytes(content, "UTF-8")
content = content.decode("UTF-8")
print(content)






