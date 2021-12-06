# we will dicuss differnt layout of the website and get the information from the page we can also make changing to the typeof the page 

import requests
from bs4 import BeautifulSoup
# define a Object and methods to it 
class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

# return the page or HTML
def getPage(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser')

# find h1 tag or main contain of page 
def scrapeNYTimes(url):
    bs = getPage(url)
    title = bs.find('h1').text
    lines = bs.select('div.StoryBodyCompanionColumn div p')
    body = '\n'.join([line.text for line in lines])
    return Content(url, title, body)

def scrapeBrookings(url):
    bs = getPage(url)
    title = bs.find('h1').text
    body = bs.find('div', {'class', 'post-body'}).text
    return Content(url, title, body)


url = 'https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/'
content = scrapeBrookings(url)
print('Title: {}'.format(content.title))
print('URL: {}\n'.format(content.url))
print(content.body)

url = 'https://www.nytimes.com/2018/01/25/opinion/sunday/silicon-valley-immortality.html'
content = scrapeNYTimes(url)  
print('Title: {}'.format(content.title))  #gives out the Title of the web page 
print('URL: {}\n'.format(content.url))  # Give  enter url of page
print(content.body)   #Manin Body or Contain of page 