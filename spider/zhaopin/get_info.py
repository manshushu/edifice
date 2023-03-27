import requests
import json
import pandas as pd
import time

# url = 'https://www.5iai.com/#/jobList'
# response = requests.get(url)
# response.text

for i in range(1, 51):
    url = 'https://www.5iai.com/api/enterprise/job/public/es?pageSize=10&pageNumber={}'.format(i)    # 一级页面网址
    print('正在爬取第 {} 页数据'.format(i))
    response = requests.get(url)             # 发送访问请求
    json_text = json.loads(response.text)    # 将返回的字符串转换成字典

    data = pd.DataFrame(json_text['data']['content'])   # 将目标数据转为数据框结构

    data['detailedAddress'] = data['enterpriseAddress'].apply(lambda x: x['detailedAddress'])    # 工作地址
    data['city'] = data['enterpriseAddress'].apply(lambda x: x['cityCode'])        # 工作城市

    data['shortName'] = data['enterpriseExtInfo'].apply(lambda x: x['enterpriseId'])       # 公司名
    data['industry'] = data['enterpriseExtInfo'].apply(lambda x: x['labelName'])         # 所属行业
    data['personScope'] = data['enterpriseExtInfo'].apply(lambda x: x['labelTypeId'])   # 人员规模
    data['econKind'] = data['enterpriseExtInfo'].apply(lambda x: x['econKind'])         # 企业性质

    # 要保留的字段
    colNames = [
        'positionName', 'minimumWage', 'maximumWage', 'exp',
        'educationalRequirements', 'detailedAddress', 'city',
        'shortName', 'industry', 'personScope', 'econKind'
    ]
    data_drop = data[colNames]       # 保留一级页面的目标字段

    jobDes = []                      # 预置空列表，用于保存二级页面中间数据
    for id in data['id']:
        sub_url = 'https://www.5iai.com/api/enterprise/job/public?id={}'.format(id)   # 二级页面网址
        sub_response = requests.get(sub_url)              # 访问二级页面
        sub_text = json.loads(sub_response.text)          # 将二级页面的返回数据转为字典
        jobDesMid = sub_text['data']['jobRequiredments']     # 职位描述
        jobDes.append(jobDesMid)                             # 保存各招聘信息的职位描述
        time.sleep(2)

    data_drop['jobDes'] = jobDes     # 保存二级页面数据

    try:
        data_drop.to_csv('information.csv', header=None, index=None, encoding='utf-8-sig', mode='a+')   # 保存数据
    except:
        print('当前页面数据写入失败，进行下一个页面数据的爬取')
