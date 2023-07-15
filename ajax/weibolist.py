import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
from pymongo import MongoClient


since_id = 0
base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
client = MongoClient()
db = client['weibo']
collection = db['weibo']
max_page = 10

def get_start_page():
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'since_id': '0'
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

def get_since_id(json):
    items = json.get('data').get('cardlistInfo')
    since_id = items['since_id']
    return since_id

def get_page(since_id):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'since_id': since_id
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        next_since_id = json.get('data').get('cardlistInfo').get('since_id')
        print(next_since_id)
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo

def save_to_mongo(result):
    if collection.insert_one(result):
        print('Saved to Mongo')

if __name__ == '__main__':
    json = get_start_page()
    since_id = get_since_id(json)
    results = parse_page(json)
    for result in results:
        print(result)
        save_to_mongo(result)
    for page in range(1, max_page + 1):
        json = get_page(since_id)
        since_id = get_since_id(json)
        results = parse_page(json)
        for result in results:
            print(result)
            save_to_mongo(result)
