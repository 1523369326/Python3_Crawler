from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from time import sleep
import requests
import json

start_url = 'https://so.toutiao.com/search?' 
def get_url(page_num):
    params = {
        'keyword': '街拍',
        'pd':'atlas',
        'dvpf':'pc',
        'aid':'4916',
        'page_num': page_num,
        'search_json': '{"from_search_id":"2023071420525404FD5975EC94B35F4C84","origin_keyword":"街拍","image_keyword":"街拍"}',
        'rawJSON': '1',
    }
    url = start_url + urlencode(params)
    return url

def get_html(url):
    driver = webdriver.Chrome()
    driver.get(url)
    sleep(5) # 等待页面加载完成
    # 获取响应内容
    html = driver.page_source  # 获取页面源码
    return html

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    # 提取数据
    json_data = json.loads(soup.pre.string)
    raw_data = json_data.get('rawData')
    if raw_data:
        data_list = raw_data.get('data')
        for item in data_list:
            text = item.get('text')
            img_url = item.get('img_url')
            print('Text:', text)
            print('Image URL:', img_url)
            print('---')
            download_image(img_url,text)

def download_image(img_url,img_name):
    music=requests.get(img_url)
    #文件名去除特殊符号
    with open("D:/6.python/10、python3实战爬虫/ajax/down_img/{}.jpeg".format(img_name),"wb") as m:
         m.write(music.content)

if __name__ == '__main__':
    for i in range(1, 11):
        url = get_url(i)
        html = get_html(url)
        parse_html(html)
        