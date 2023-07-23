**爬取第二届中国国际储能展会文档**

本文档介绍了使用Python编写的爬虫程序，用于爬取第二届中国国际储能展会的展商名录、参展展品、投票页等信息，包括文字和图片内容，并将数据保存到本地。该爬虫程序通过拦截网络流量并使用mitmdump工具来实现数据的获取和处理。

**目标网站和数据获取方式：**
- 网站：第二届中国国际储能展会相关页面
- 数据获取方式：通过拦截小程序网络流量，分析链接和接口，获取展商名录、参展展品和投票页等信息的URL。

**工具和库：**
- mitmdump：用于拦截小程序的网络流量，获取数据。
- Python库：包括urllib.parse、pandas、json等库。

**运行环境：**
- Python 3.9及以上版本。

**功能实现：**
1. 使用mitmdump工具拦截小程序的网络流量，并分析链接和接口，获取展商名录、参展展品和投票页等信息的URL。
2. 根据获取的URL，发送请求获取相应的数据，并解析JSON数据格式。
3. 提取展商名录、参展展品和投票页等信息，并将照片URL拼接为完整URL。
4. 将提取的数据存储在内存中，分别保存为Python列表exhibit_data和exhibitors_data。
5. 将展商名录数据exhibit_data保存到Excel文件'data_exhibit.xlsx'中，将参展展品数据exhibitors_data保存到Excel文件'data_exhibitors.xlsx'中。
6. 将照片保存到本地文件夹中。

**代码结构：**
1. 导入所需的Python库和模块。
2. 定义照片URL前缀url_first，用于拼接照片的完整URL。
3. 创建全局变量exhibit_data和exhibitors_data，用于存储展商名录和参展展品数据。
4. 编写mitmdump的response函数，通过URL匹配对应的页面数据。
5. 在response函数中提取数据，并将照片URL拼接为完整URL，然后分别存储在exhibit_data和exhibitors_data中。
6. 编写保存数据到Excel文件的函数save_to_excel，将exhibit_data和exhibitors_data中的数据保存到不同的Excel文件中。
7. 使用atexit库，在程序结束时自动调用save_to_excel函数，将数据保存到Excel文件中。
8. 最后的文档末尾，提示运行环境、功能实现、代码结构等信息，以及必要的运行步骤。

**注意事项：**
- 确保运行环境中安装了Python 3.9及以上版本，并安装了所需的Python库和mitmdump工具。
- 在运行爬虫程序之前，先运行上述代码，然后再运行mitmdump命令，以拦截网络流量并执行爬虫程序。
- 在程序运行过程中，爬取的数据将存储在内存中，直到程序结束时，才会将数据保存到Excel文件和照片保存到本地文件夹。





