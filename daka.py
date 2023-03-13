# 是时候来个小项目了，具体我的想法如下：
# 1.登录认证
# 2.开始模拟  跑到第一个点然后发送第一个点打卡，直到四个点都结束
# 3. 判断是否跑到2km 时间是否在指标内 结束跑步
# 上传
# 做成每天的自动任务
# coding:utf-8\
# 抓包加模拟罢了，注意抽象层级
# User-Agent:
# {"status":"success","data":{"openId":"oaggy5c4IUIUqUIaBwzDcktRirzA","sex":"1","accountNumber":"200141933","userName":"满智杰","type":"1","userId":"2990600592c04b13b812041a2c630317"}}
import requests
import json
import urllib3
urllib3.disable_warnings()
# 请求地址
loginurl = "https://cpapp.1lesson.cn//api/user/login"
data = {
    "userAccount": "200141933",
    "openId": "oaggy5c4IUIUqUIaBwzDcktRirzA",
    "userPassword": "123456",
}
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat"
}
firstrequest = requests.post(loginurl, data=data, verify=False, headers=headers)
# 登陆成功！！！
# 接下来应该提取userid
# print(r.json())
temp = firstrequest.json()
# print(temp)
userId = temp["data"]["userId"]

url2 = "https://cpapp.1lesson.cn/api/route/selectStudentRunningRecord"
data2 = {"userId": userId}
secondrequest = requests.post(url2, data=data2, verify=False, headers=headers)
# print(secondrequest.json())


url3 = "https://cpapp.1lesson.cn/api/route/selectRandomRoute"
data3 = {
    "userID": "2990600592c04b13b812041a2c630317",
    "posLongitude": "30.838973",
    "posLatitude": "121.511462",
}

routerequest=requests.post(url3, data=data3, verify=False, headers=headers)


url4="https://cpapp.1lesson.cn/api/route/selectRoute"
data4={"userId": userId}
selectrequest=requests.post(url4, data=data4, verify=False, headers=headers)


url5="https://cpapp.1lesson.cn/api/route/insertStartRunning"
data5={"userId": userId}
startrequest=requests.post(url5, data=data5, verify=False, headers=headers)
