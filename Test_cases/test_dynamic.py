"""
version : v0.9.1
author: chenjie
"""
from Common import method
from Params.read_yml import read_data,read_url
import pytest
from Config.read_config import projectId,userId

@pytest.fixture(name="dynamicId",scope='module')
def test_add_dynamic(get_headers_json):
    """
    发布动态（带图片/文件/任务）
    :param get_headers_json:
    :return: dynamicId
    """
    url = read_url(1)
    json = read_data(1)
    headers = get_headers_json
    r = method.HttpRequest()
    res = r.run_method(url=url, method="POST", json=json, headers=headers)
    return res.json()["resModel"] #返回动态id

@pytest.fixture(name="remarkId",scope='module')
def test_add_dynamic_remark(get_headers_json,dynamicId):
    """
    动态评论
    :param get_headers_json:
    :param dynamicId:
    :return: remarkId
    """
    url = read_url(2)
    json = {"content":"测试","dynamicId":dynamicId,"projectId":projectId(),"imgs":[]}
    headers = get_headers_json
    r = method.HttpRequest()
    res = r.run_method(url=url, method="POST", json=json, headers=headers)
    return res.json()["resModel"]["id"] #返回评论的id

def test_addRemarkResponse(get_headers_json,dynamicId,remarkId):
    """
    回复评论
    :param get_headers_json:
    :param dynamicId:
    :param remarkId:
    :return:
    """
    url = read_url(3)
    json = {"content":"测试","dynamicId":dynamicId,"projectId":projectId(),"imgs":[],"remarkId":remarkId,"responseeUserId":userId()}
    headers = get_headers_json
    r = method.HttpRequest()
    r.run_method(url=url, method="POST", json=json, headers=headers)

def test_addLaud(get_headers,dynamicId):
    """
    动态点赞
    :param dynamicId:
    :return:
    """
    url = read_url(4)
    headers = get_headers
    data={"dynamicId":dynamicId,"projectId":projectId()}
    r = method.HttpRequest()
    r.run_method(url=url, method="POST", data=data, headers=headers)

@pytest.mark.testdel
def test_deleteLaud(get_headers_json,dynamicId):
    """
    动态取消点赞
    :param get_headers_json:
    :param dynamicId
    :return:
    """
    url = read_url(5)
    params = {"dynamicId":dynamicId,"projectId":projectId()}
    headers = get_headers_json
    r = method.HttpRequest()
    r.run_method(url=url, method="del",headers=headers,params=params)

def test_dynamic_detail(get_headers_json,dynamicId):
    """
    查询动态详情
    :param get_headers_json:
    :param dynamicId:
    :return:
    """
    url = read_url(6)
    headers = get_headers_json
    data={"id":dynamicId,"projectId":projectId()}
    r = method.HttpRequest()
    r.run_method(url=url, method="get", data=data, headers=headers)

@pytest.mark.testdel
def test_del_dynamic_remark(get_headers_json,dynamicId,remarkId):
    """
    删除评论
    :param get_headers_json:
    :param dynamicId:
    :param remarkId:
    :return:
    """
    url =read_url(7)
    params = {"dynamicId":dynamicId,"projectId":projectId(),"remarkId":remarkId}
    headers = get_headers_json
    r = method.HttpRequest()
    r.run_method(url=url, method="del",headers=headers,params=params)

@pytest.mark.testdel
def test_del_dynamic(get_headers_json,dynamicId):
    """
    删除动态
    :param get_headers_json:
    :param dynamicId:
    :return:
    """
    url = read_url(8)
    params = {"id":dynamicId}
    headers = get_headers_json
    r = method.HttpRequest()
    r.run_method(url=url, method="del",headers=headers,params=params)

if __name__ == '__main__':
    pytest.main(["-s","D:/Pycharm/API_Atuo/Test_cases/test_dynamic.py"])
