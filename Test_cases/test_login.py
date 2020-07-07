"""
version : v0.9.1
author: chenjie
"""
import pytest
from Common import method
from Params.read_yml import read_data,read_url
from Config.read_config import appId

def test_login():
    '''
    登陆
    :return:
    '''
    url=read_url(0)
    headers = {"Accept": "*/*", "appId": appId()}
    data = read_data(0)
    r=method.HttpRequest()
    res =r.run_method(url=url,method="POST",data=data,headers=headers)
    # print(res.json())
    return (res.json()["resModel"]["token"])

if __name__ == '__main__':
    pytest.main(["-s","D:/Pycharm/API_Atuo/Test_cases/test_login.py"])