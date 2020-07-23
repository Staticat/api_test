"""
version : v0.9.1
author: chenjie
"""
from Common import method
from Params.rw_yml import read_data,read_url,set_data_yaml
import pytest
"""
此用例为设计任务从创建到验证合格过程
"""

def test_add_task2(get_headers_json):
    """
    添加设计任务
    :param get_headers_json:
    :return:taskId1
    """
    url = read_url(9)
    headers=get_headers_json
    json = read_data(18)
    r = method.HttpRequest()
    res = r.run_method(url=url, method="POST", json=json, headers=headers)
    taskId = res.json()["resModel"]
    set_data_yaml("taskId",taskId)  # 任务id写入data.yaml文件
    set_data_yaml("id",taskId)  # 任务id写入data.yaml文件

def test_startDesignTask(get_headers_json):
    """
    开始设计任务
    :param get_headers_json:
    :param taskId2:
    :return:
    """
    url = read_url(14)
    headers = get_headers_json
    json = read_data(19)
    r = method.HttpRequest()
    r.run_method(url=url, method="POST", json=json, headers=headers)

def test_taskDeliverables_add(get_headers_json):
    """
    提交设计成果
    :param get_headers_json:
    :param taskId2:
    :return:
    """
    url = read_url(15)
    headers = get_headers_json
    json = read_data(20)
    r = method.HttpRequest()
    r.run_method(url=url, method="POST", json=json, headers=headers)

def test_detail_task3(get_headers_json):
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
    actTaskId=res.json()["resModel"]["activitiMap"]['currentTaskList'][0]['id']
    set_data_yaml("actTaskId", actTaskId)

def test_submitDesignVerify(get_headers_json):
    """
    设计任务提交审核
    :param get_headers_json:
    :return:
    """
    url = read_url(16)
    headers = get_headers_json
    json = read_data(21)
    r = method.HttpRequest()
    r.run_method(url=url, method="POST", json=json, headers=headers)

def test_detail_task4(get_headers_json):
    """
    查看任务详情，返回任务检验节点id
    :param get_headers_json:
    :param taskId1:
    :return: processInstanceId
    """
    url = read_url(11)
    headers=get_headers_json
    data =  read_data(11)
    r = method.HttpRequest()
    res = r.run_method(url=url, method="get", data=data, headers=headers)
    actTaskId=res.json()["resModel"]["activitiMap"]['currentTaskList'][0]['id']
    set_data_yaml("actTaskId", actTaskId)

def test_designVerify(get_headers_json):
    url = read_url(17)
    headers = get_headers_json
    json =  read_data(22)
    r = method.HttpRequest()
    r.run_method(url=url, method="POST", json=json, headers=headers)

if __name__ == '__main__':
    pytest.main(["-v","D:/Pycharm/API_Atuo/Test_cases/test_task2.py"])