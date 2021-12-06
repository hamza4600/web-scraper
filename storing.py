# we will download the data from the web sites
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
# simply we can type the id of the div that have the imgs we wil get them
html = urlopen('https://cp-algorithms.com/')
bs = BeautifulSoup(html, 'html.parser')
imageLocation = bs.find('a', {'id': 'logo'}).find('img')['src']
urlretrieve (imageLocation, 'logo.jpg')
