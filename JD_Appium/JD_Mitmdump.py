import json
import pymongo

client = pymongo.MongoClient('localhost')
db = client['jd']
products_collection = db['products']

def response(flow):
    url = 'api.m.jd.com/'
    # 如果url出现在flow.request.url中，在执行下面的函数
    if url in flow.request.url:
        text = flow.response.text
        data = json.loads(text)
        shops = data.get('wareInfo')
        for shop in shops:
            item = {
                'spuId': shop.get('spuId'),
                'wname': shop.get('wname'),
                'price': shop.get('jdPrice'),
                'reviews': shop.get('reviews')
            }
            products_collection.insert_one(item)
            print(item)
            #写入MongoDB数据库
            #collection.insert(data)

