import requests,time,random,json,re
from urllib.parse import urlencode
#import pymongo
from requests.exceptions import RequestException


def get_pages(since_id):
    data = {
           
        'type': 'uid',
        'value':'2830678474',
        'containerid':'1076032830678474',
        'since_id': since_id
        }
    
    base_url = 'https://m.weibo.cn/api/container/getIndex?'
    url = base_url + urlencode(data)
    result = requests.get(url,headers = headers)
    try:
        if result.status_code==200:
             print(result.json()) ###网页的返回类型实际上是 str 类型，但是它很特殊，是 JSON 格式的 所以，如果想直接
                                       ###  解析返回结果，得到一个字典格式的话，可以直接调用json()方法
    except requests.ConnectionError as e:
            print('Error',e.args)


            
            

min_since_id = ''
def get_since_id():
    
    global min_since_id
    topic_url ='https://m.weibo.cn/api/container/getIndex?uid=2830678474&luicode=10000011&lfid=1076032830678474&type=uid&value=2830678474&containerid=1076032830678474'
    topic_url = topic_url+'&since_id='+str(min_since_id)
    ##print(json)
    result = requests.get(topic_url,headers = headers)
    json = result.json()
    #print(json)
    items = json.get('data').get('cardlistInfo')
    #print(items)
    min_since_id=items['since_id' ]
    return min_since_id



def main():
   
    for i in range(10):
        print('第{}页'.format(i))
        print(get_since_id())
        get_pages(get_since_id())
      
        

#def save_to_mongodb(dict):
#    
#    client = pymongo.MongoClient()
#    db = client['weibo']
#    collection = db['weibo']
#    if collection.insert_one(dict):  #返回ID值
#         print('写入数据成功！')
#         #print(result.inserted_ids)###返回插入数据的id列表
       
    
        

if __name__ == '__main__':
    
    headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
            }
    main()
 
