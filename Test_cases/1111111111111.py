from Common import method
import requests
from Params import read_yml
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

print(method.get_url(0))
