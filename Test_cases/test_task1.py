"""
version : v0.9.1
author: chenjie
"""
from Common import method
from Params.rw_yml import read_data,read_url,set_data_yaml
import pytest
import json
"""
此用例为施工任务（非签章任务）从创建到点击合格过程
"""

def test_add_task1(get_headers_json):
    """
    添加施工任务
    :param get_headers_json:
    :return:taskId
    """
    url = read_url(9)
    headers=get_headers_json
    json = read_data(8)
    r = method.HttpRequest()
    res = r.run_method(url=url, method="POST", json=json, headers=headers)
    taskId = res.json()["resModel"]
    set_data_yaml("taskId",taskId)  # 任务id写入data.yaml文件
    set_data_yaml("id",taskId)  # 任务id写入data.yaml文件

def test_start_task(get_headers_json):
    """
    开始任务
    :param get_headers_json:
    :return:
    """
    url = read_url(12)
    headers = get_headers_json
    json = read_data(9)
    r = method.HttpRequest()
    res=r.run_method(url=url, method="POST", json=json, headers=headers)
    print(res.text)

def test_finish_task(get_headers_json):
    """
    通过发布动态关联任务，100%触发完成任务
    :param get_headers_json:
    :return:
    """
    url = read_url(1)
    headers = get_headers_json
    json = read_data(10)
    r = method.HttpRequest()
    res=r.run_method(url=url, method="POST", json=json, headers=headers)
    print(res.text)

def test_detail_task1(get_headers_json):
    """
    查看任务详情，返回任务完成节点id
    :param get_headers_json:
    :param taskId1:
    :return: processInstanceId
    """
    url = read_url(11)
    headers=get_headers_json
    data = read_data(11)
    r = method.HttpRequest()
    res = r.run_method(url=url, method="get", data=data, headers=headers)
    actTaskId = res.json()["resModel"]["activitiMap"]['currentTaskList'][0]['id']
    set_data_yaml('actTaskId', actTaskId)  # 任务完成节点id写入data.yaml文件

def test_submitVerify_task(get_headers_json):
    """
    任务提交检验
    :param get_headers_json:
    :param taskId1:
    :param processInstanceId:
    :return:
    """
    url = read_url(10)
    headers = get_headers_json
    json= read_data(12)
    r = method.HttpRequest()
    r.run_method(url=url, method="POST", json=json, headers=headers)

def test_detail_task2(get_headers_json):
    """
    查看任务详情，返回检验节点的id
    :param get_headers_json:
    :param taskId1:
    :return: processInstanceId
    """
    url = read_url(11)
    headers=get_headers_json
    data =  read_data(13)
    r = method.HttpRequest()
    res = r.run_method(url=url, method="get", data=data, headers=headers)
    actTaskId = res.json()["resModel"]["activitiMap"]['currentTaskList'][0]['id']
    set_data_yaml('actTaskId', actTaskId)  # 任务完成节点id写入data.yaml文件

def test_updateEnableSignFlag(get_headers_from):
    """
    取消签章功能
    :param get_headers:
    :return:
    """
    url = read_url(18)
    headers = get_headers_from
    data = read_data(15)
    r = method.HttpRequest()
    r.run_method(url=url, method="POST", data=data, headers=headers)

def test_detail_task3(get_headers_json):
    """
    查看任务详情，返回检验节点的id
    :param get_headers_json:
    :param taskId1
    :return: processInstanceId
    """
    url = read_url(11)
    headers=get_headers_json
    data =  read_data(17)
    r = method.HttpRequest()
    res = r.run_method(url=url, method="get", data=data, headers=headers)
    actTaskId = res.json()["resModel"]["activitiMap"]['currentTaskList'][0]['id']
    set_data_yaml('actTaskId', actTaskId)  # 任务完成节点id写入data.yaml文件

def test_verify(get_headers_json):
    """
    非签章任务点击合格
    :param get_headers:
    :return:
    """
    url = read_url(19)
    headers = get_headers_json
    data = read_data(16)
    r = method.HttpRequest()
    r.run_method(url=url, method="POST", data=json.dumps(data), headers=headers)

# def test_signCertificate(get_headers):
#     """
#     点击合格进入签章系统
#     :param get_headers_json:
#     :param taskId1:
#     :param actTaskId:
#     :return:
#     """
#     url = read_url(13)
#     headers = get_headers
#     data = read_data(14)
#     r = method.HttpRequest()
#     r.run_method(url=url, method="POST", data=data, headers=headers)

if __name__ == '__main__':
    pytest.main(["-v","D:/Pycharm/API_Atuo/Test_cases/test_task1.py"])