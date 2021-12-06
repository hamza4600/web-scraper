#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import os

same_url='https://pixabay.com/'
dir_name ="/usr/home/hamza/Desktop"
print('Photo directory' + dir_name)
a1 = os.path.exists(dir_name)
if not a1:
  os.makedirs(dir_name)
os.chdir(dir_name)
def download (weburl,type_dir):
    r = requests.get(weburl)
    soup = BeautifulSoup(r.text, 'lxml')
    for link in soup.find_all('a'):
        if 'article' in link.get('href'):
            list_url = 'https://pixabay.com/' + link.get('href')
            # print(list_url)
            rb = requests.get(list_url).text.encode("latin1").decode("gbk")
            soup2 = BeautifulSoup(rb, 'lxml').find_all('img')
            img_dirname = BeautifulSoup(rb, 'lxml').find('div', class_='title').get_text()
            # print (img_dirname)
            # creata folder 
            print('start download： ' + type_dir+'/'+img_dirname)

            a = os.path.exists(type_dir+'/'+img_dirname)
            if not a:
                os.makedirs(type_dir+'/'+img_dirname)
            else:
                print("Already existed if you nedd to download again delete directory")
                continue
            os.chdir(type_dir+'/'+img_dirname)
            for a in soup2:
                img_url = a['src']
                img_name = img_url[-15:-4]
                img = requests.get(img_url)
                f = open(img_name + '.jpg', 'ab')
                f.write(img.content)
                print(img_name, 'Picture Saved:' + dir_name + '\\' + img_dirname)
                f.close()
            print(img_dirname + 'Download complete')
            os.chdir(dir_name)

for i in range(16,23):
    typeurl=same_url+str(i)+'.html'
    print(typeurl)
    download(typeurl,str(i))
    r=requests.get(typeurl).text.encode("latin1").decode("gbk")
    bs=BeautifulSoup(r,'lxml').find('span').get_text()
    max_page=bs[-3:-1]
    for m in range(2,int(max_page)+1):
        weburl=same_url+str(i)+'_'+str(m)+'.html'
        print(weburl)
        download(weburl, str(i))
