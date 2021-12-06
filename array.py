# we will convert all data into a arry then we will use that array to change the some other operations on the array
from urllib.request import urlopen
from bs4 import BeautifulSoup
# a function that will add allitem to a array
def getNgrams(content, n):
  content = content.split(' ')
  output = []
  for i in range(len(content)-n+1):
    output.append(content[i:i+n])
  return output

html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bs = BeautifulSoup(html, 'html.parser')
content = bs.find('div', {'id':'mw-content-text'}).get_text()
ngrams = getNgrams(content, 2)
print(ngrams)
print('2-grams count is: '+str(len(ngrams)))