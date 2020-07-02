import pytest
from Common import method
from Params import read_yml
from Config.read_config import appId

def test_login():
    '''
    登陆
    :return:
    '''
    url=method.get_url(0)
    headers = {"Accept": "*/*", "appId": appId()}
    data = read_yml.read_data(0,'data')
    r=method.HttpRequest()
    res =r.run_method(url=url,method="POST",data=data,headers=headers)
    # print(res.json())
    return (res.json()["resModel"]["token"])

if __name__ == '__main__':
    pytest.main(["-s","D:/Pycharm/API_Atuo/Test_cases/test_login.py"])