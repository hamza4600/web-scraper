import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
# define the basic  varibles and functions
downloadDirectory = 'downloaded'
baseUrl = 'http://pythonscraping.com'
# identify the url and pattern
def getAbsoluteURL(baseUrl, source):
    if source.startswith('http://www.'):
        url = 'http://{}'.format(source[11:])
    elif source.startswith('http://'):
        url = source
    elif source.startswith('www.'):
        url = source[4:]
        url = 'http://{}'.format(source)
    else:
        url = '{}/{}'.format(baseUrl, source)
    if baseUrl not in url:
        return None
    return url
# pathe where to download the a file
def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace('www.', '')
    path = path.replace(baseUrl, '')
    path = downloadDirectory+path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)

    return path
# open the page and get the data
html = urlopen('http://www.pythonscraping.com')
bs = BeautifulSoup(html, 'html.parser')
downloadList = bs.findAll(src=True) #find all items having asource and get them

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download['src'])
    if fileUrl is not None:
        print(fileUrl)

# it will  retun a lsit of all download data in forn of Links 
print(downloadList)
# urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))