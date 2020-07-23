"""
version : v0.9.1
author: chenjie
"""
import pytest
from Common import method
from Params.rw_yml import read_data,read_url,set_headers_yaml
from Config.read_config import appId,openId,projectId

def test_login():
    '''
    登陆
    :return:
    '''
    set_headers_yaml("openId", openId()) #初始化登陆信息
    set_headers_yaml("projectId", projectId()) #初始化项目ID信息
    url=read_url(0)
    headers = {"Accept": "*/*", "appId": appId()}
    data = read_data(0)
    r=method.HttpRequest()
    res=r.run_method(url=url,method="POST",data=data,headers=headers)
    return res.json()["resModel"]["token"]
    # set_headers_yaml("token",res.json()["resModel"]["token"])
    # set_headers_yaml("appId",appId())

if __name__ == '__main__':
    pytest.main(["-s","D:/Pycharm/API_Atuo/Test_cases/test_1login.py"])