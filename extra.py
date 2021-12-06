import requests
from bs4 import BeautifulSoup
import os
import threading
# url = 'http://a.66d.club'

same_url = '/'
url = '/'
rq = requests.get(url).text.encode('latin1').decode('utf-8')
bs = BeautifulSoup(rq, 'lxml').find('div', class_='box dy_list').find_all('a')
video_save_path = '/data/video/tmp/'

if not os.path.exists(video_save_path):
    os.makedirs(video_save_path)
os.chdir(video_save_path)

threads = []


def download(videourl, num):
    video_url = videourl+'/video'+str(num)+'.ts'
    video_name = str(num)+'.ts'
    print('start download：', video_name)
    video = requests.get(video_url)
    f = open(video_name, 'wb')
    f.write(video.content)
    f.close()
    print(video_name, 'Dowwnload complet')


for i in range(0, len(bs)):
    video_name = bs[i]['title']
    
    video_url = same_url+bs[i]['href'].replace('vod', 'vodplay')
    # print(video_name, video_url.replace('vod','vodplay'))
    rq = requests.get(video_url).text.encode('latin1').decode('utf-8')
    
    video_m3u8 = rq[rq.find('video:[[\'') +9:rq.find('0],]') - 8]
   
    
    if requests.get(video_m3u8).content[-22:-19].isdigit():
        max_num = requests.get(video_m3u8).content[-22:-19]
    elif requests.get(video_m3u8).content[-21:-19].isdigit(): 
        max_num = requests.get(video_m3u8).content[-21:-19]
    else:
        max_num = requests.get(video_m3u8).content[-20:-19]
    
    video_m3u8_sameurl = video_m3u8[:video_m3u8.find('video')]
    # print(video_name, video_m3u8_sameurl, rq_m3u8_max_num)
    # 
    if not os.path.exists(video_name):
        print('start download:',video_name) 
        os.makedirs(video_name)
        os.chdir(video_name)
        for i in range(1, int(max_num) + 1):
            download(video_m3u8_sameurl,i)
        print(video_name,'Completed;')
    else:
        continue
    os.chdir(video_save_path)
