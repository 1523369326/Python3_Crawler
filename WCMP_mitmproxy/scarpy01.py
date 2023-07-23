from urllib.parse import unquote
import pandas as pd
import json

# 拼接图片url
url_first = 'https://storageenergy.oss-accelerate.aliyuncs.com'

# 创建一个全局变量用于保存所有数据
data_all_url1 = []
data_all_url2 = []

def response(flow):
    # 提取参展商品
    url1 = 'https://platform.innoempower.com/eesa-home/exhibitor/exhibit/applet/v1.0/listByProductKindId'
    # 展商目录
    url2 = 'https://platform.innoempower.com/eesa-home/exhibitor/exhibitors/applet/v1.0/listByPavilionsId'
    
    global data_all_url1, data_all_url2  # 声明使用全局变量

    if url1 in flow.request.url:
        text = flow.response.text
        data = json.loads(text)
        shops = data.get('datas').get('records')
        for shop in shops:
            item01 = {}
            item_id = shop.get('id')
            item_name = shop.get('name')
            item_exhibitorsName = shop.get('exhibitorsName')
            item_pic_url = url_first + shop.get('pic')
            item_pavilionName = shop.get('pavilionName')
            item_position = shop.get('position')
            item_heat = shop.get('heat')
            item01 = {'id': item_id, 'name': item_name, 'exhibitorsName': item_exhibitorsName, 'pic_url': item_pic_url,
                      'pavilionName': item_pavilionName, 'position': item_position, 'heat': item_heat}
            data_all_url1.append(item01)
            print(item01)

    elif url2 in flow.request.url:
        text = flow.response.text
        data = json.loads(text)
        shops = data.get('datas').get('records')
        for shop in shops:
            item02 = {
                'id': shop.get('id'),
                'exhibitorsName': shop.get('exhibitorsName'),
                'enterpriseLogo': shop.get('enterpriseLogo'),
                'position': shop.get('position'),
                'pavilionName': shop.get('pavilionName'),
                'heat': shop.get('heat'),
            }
            data_all_url2.append(item02)
            print(item02)

def save_to_excel(data, filename):
    data_df = pd.DataFrame(data)
    # 将数据保存为 Excel 文件
    data_df.to_excel(filename, index=False)

# 在程序结束时调用保存函数，保存两个文件
import atexit

atexit.register(save_to_excel, data_all_url1, 'data_url1.xlsx')
atexit.register(save_to_excel, data_all_url2, 'data_url2.xlsx')
