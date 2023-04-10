import requests
import json
import pandas as pd
import time

# url = 'https://www.5iai.com/#/jobList'
# response = requests.get(url)
# response.text


url = 'http://www.tcmdoc.cn/ShuJuKu/XueWei/index.aspx'    # 一级页面网址
# print('正在爬取第 {} 页数据'.format(i))
response = requests.get(url)             # 发送访问请求
json_text = json.loads(response.text) 