"""
version : v0.9.1
author: chenjie
"""
from Common import method
from Params.read_yml import read_data,read_url
import pytest
from Config.read_config import projectId,userId

"""
此用例为设计任务从创建到验证合格过程
"""
@pytest.fixture(name="taskId2",scope='module')
def test_add_task2(get_headers_json):
    """
    添加设计任务
    :param get_headers_json:
    :return:taskId1
    """
    url = read_url(9)
    headers=get_headers_json
    json = read_data(3)
    r = method.HttpRequest()
    res = r.run_method(url=url, method="POST", json=json, headers=headers)
    return res.json()["resModel"]  # 返回任务id

def test_startDesignTask(get_headers_json,taskId2):
    """
    开始设计任务
    :param get_headers_json:
    :param taskId2:
    :return:
    """
    url = read_url(14)
    headers = get_headers_json
    json = {"content":"测试设计任务今日开始","imgList":[],"taskId":taskId2,"receiveUserIdList":[],"receiveTeamIdList":[]}
    r = method.HttpRequest()
    r.run_method(url=url, method="POST", json=json, headers=headers)

def test_taskDeliverables_add(get_headers_json,taskId2):
    """
    提交设计成果
    :param get_headers_json:
    :param taskId2:
    :return:
    """
    url = read_url(15)
    headers = get_headers_json
    json = {"content":"测试提交成果","fileIdList":[],"imgList":[],"videoList":[],"taskId":taskId2}
    r = method.HttpRequest()
    r.run_method(url=url, method="POST", json=json, headers=headers)

@pytest.fixture(name="actTaskId3",scope='module')
def test_detail_task3(get_headers_json,taskId2):
    """
    查看任务详情，返回任务完成节点id
    :param get_headers_json:
    :param taskId1:
    :return: processInstanceId
    """
    url = read_url(11)
    headers=get_headers_json
    data = {"id":taskId2}
    r = method.HttpRequest()
    res = r.run_method(url=url, method="get", data=data, headers=headers)
    return res.json()["resModel"]["activitiMap"]['currentTaskList'][0]['id']

def test_submitDesignVerify(get_headers_json,taskId2,actTaskId3):
    url = read_url(16)
    headers = get_headers_json
    json = {"actTaskId":actTaskId3,"content":"设计任务提交审核","imgList":[],"taskId":taskId2,"overwriteVerifyUserIdList":[userId()]}
    r = method.HttpRequest()
    r.run_method(url=url, method="POST", json=json, headers=headers)

@pytest.fixture(name="actTaskId4",scope='module')
def test_detail_task4(get_headers_json,taskId2):
    """
    查看任务详情，返回任务检验节点id
    :param get_headers_json:
    :param taskId1:
    :return: processInstanceId
    """
    url = read_url(11)
    headers=get_headers_json
    data = {"id":taskId2}
    r = method.HttpRequest()
    res = r.run_method(url=url, method="get", data=data, headers=headers)
    return res.json()["resModel"]["activitiMap"]['currentTaskList'][0]['id']

def test_designVerify(get_headers_json,taskId2,actTaskId4):
    url = read_url(17)
    headers = get_headers_json
    json = {"actTaskId":actTaskId4,"content":"测试审核通过","fileIdList":[],"imgList":[],"videoList":[],"pass":1,"taskId":taskId2,"receiveTeamIdList":[],"receiveUserIdList":[]}
    r = method.HttpRequest()
    r.run_method(url=url, method="POST", json=json, headers=headers)

if __name__ == '__main__':
    pytest.main(["-v","D:/Pycharm/API_Atuo/Test_cases/test_task2.py"])