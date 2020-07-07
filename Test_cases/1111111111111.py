from Common import method
import requests
from Params.read_yml import read_data,read_url
from Config.read_config import projectId
import pytest
# import json
# data = read_yml.read_data(1,'data')
# data1 = read_yml.read_data(0,'data')
# print(data)
# print(data1)
# print(type(data))
#
# from Config.read_config import appId
# print(appId())
import pytest

#
# @pytest.fixture()
# def test_01():
#     a=1
#     return a
#
# def test_02(test_01):
#     c =test_01+1
#     print(c)
#
# if __name__ == '__main__':
#     pytest.main(["-s","D:/Pycharm/API_Atuo/1111111111111.py"])
# @pytest.fixture()
# def test_01(get_token):
#     a=get_token
#     return a
#
# def test_02(test_01):
#     b=test_01
#     print(b)
#     return b
#

# @pytest.mark.parametrize("test_02",[test_02(test_01())])
# def test_03(test_02):
#     c=test_02+"1"
#     print(c)
#     return c

# res= requests.get("https://componentprd.tgct.com.cn/api/bigscreenservice/bigScreenIndex/getCompanyMeetingList?companyId=710171157168390181&meetingStatus=&title=&currentPage=1&pageSize=999")
# print(res.json()["totalRows"])
# # print(type(res.json()["totalRows"]))
# a=[]
# for i in range(res.json()["totalRows"]):
#     # print(res.json()["resModel"][i]["id"])
#     a.append(res.json()["resModel"][i]["id"])
# print(a)

# def submitVerify_task():
#     url = read_url(10)
#     headers={'Accept': '*/*', 'Content-Type': 'application/json', 'appId': 'wxcd03432c1d3bfcb7', 'token': '5bfe5f7a-6458-4e33-b605-1fe326a25c96'}
#     json={"content":"提交检验","imgList":[],"taskId":"728324033623359516","receiveUserIdList":[],"receiveTeamIdList":[],"actTaskId":475380,"overwriteVerifyUserIdList":["513042573758038021"]}
#     r = method.HttpRequest()
#     res= r.run_method(url=url, method="POST", json=json, headers=headers)
#     print(res.text)
# submitVerify_task()

def submitDesignVerify():
    url = read_url(16)
    headers = {'Accept': '*/*', 'Content-Type': 'application/json', 'appId': 'wxcd03432c1d3bfcb7', 'token': '5bfe5f7a-6458-4e33-b605-1fe326a25c96'}
    json = {"actTaskId":'473619',"content":"设计任务提交审核","imgList":[],"taskId": '728324033623359602',"overwriteVerifyUserIdList":[userId()]}
    r = method.HttpRequest()
    res= r.run_method(url=url, method="get", json=json, headers=headers)
    print(res.text)

submitDesignVerify()