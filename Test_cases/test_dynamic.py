"""
version : v0.9.1
author: chenjie
"""
from Common import method
from Params.rw_yml import read_data,read_url,set_data_yaml
import pytest

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
    dynamicId=res.json()["resModel"]
    set_data_yaml("dynamicId",dynamicId) #动态id写入data.yaml文件
    set_data_yaml("id",dynamicId) #动态id写入data.yaml文件

def test_add_dynamic_remark(get_headers_json):
    """
    动态评论
    :param get_headers_json:
    :param dynamicId:
    :return: remarkId
    """
    url = read_url(2)
    json = read_data(2)
    headers = get_headers_json
    r = method.HttpRequest()
    res = r.run_method(url=url, method="POST", json=json, headers=headers)
    remarkId=res.json()["resModel"]["id"]
    set_data_yaml("remarkId",remarkId) #评论id写入data.yaml文件

def test_addRemarkResponse(get_headers_json):
    """
    回复评论
    :param get_headers_json:
    :return:
    """
    url = read_url(3)
    json = read_data(3)
    headers = get_headers_json
    r = method.HttpRequest()
    r.run_method(url=url, method="POST", json=json, headers=headers)

def test_addLaud(get_headers):
    """
    动态点赞
    :param get_headers:
    :return:
    """
    url = read_url(4)
    headers = get_headers
    data= read_data(4)
    r = method.HttpRequest()
    r.run_method(url=url, method="POST", data=data, headers=headers)

@pytest.mark.testdel
def test_deleteLaud(get_headers_json):
    """
    动态取消点赞
    :param get_headers_json:
    :param dynamicId
    :return:
    """
    url = read_url(5)
    params = read_data(4)
    headers = get_headers_json
    r = method.HttpRequest()
    r.run_method(url=url, method="del",headers=headers,params=params)

def test_dynamic_detail(get_headers_json):
    """
    查询动态详情
    :param get_headers_json:
    :param dynamicId:
    :return:
    """
    url = read_url(6)
    headers = get_headers_json
    data = read_data(7)
    r = method.HttpRequest()
    r.run_method(url=url, method="get", data=data, headers=headers)

@pytest.mark.testdel
def test_del_dynamic_remark(get_headers_json):
    """
    删除评论
    :param get_headers_json:
    :param dynamicId:
    :param remarkId:
    :return:
    """
    url =read_url(7)
    params = read_data(5)
    headers = get_headers_json
    r = method.HttpRequest()
    r.run_method(url=url, method="del",headers=headers,params=params)

@pytest.mark.testdel
def test_del_dynamic(get_headers_json):
    """
    删除动态
    :param get_headers_json:
    :param dynamicId:
    :return:
    """
    url = read_url(8)
    params = read_data(6)
    headers = get_headers_json
    r = method.HttpRequest()
    r.run_method(url=url, method="del",headers=headers,params=params)

if __name__ == '__main__':
    pytest.main(["-s","D:/Pycharm/API_Atuo/Test_cases/test_dynamic.py"])
