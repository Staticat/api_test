"""
version : v0.9.1
author: chenjie
"""
from Common import method
from Params.read_yml import read_data,read_url
import pytest
from Config.read_config import projectId,userId

"""
此用例为施工任务从创建到点击合格过程，签章对外接入，因此签章将不做入自动化接口
"""

@pytest.fixture(name="taskId1",scope='module')
def test_add_task1(get_headers_json):
    """
    添加施工任务
    :param get_headers_json:
    :return:taskId1
    """
    url = read_url(9)
    headers=get_headers_json
    json = read_data(2)
    r = method.HttpRequest()
    res = r.run_method(url=url, method="POST", json=json, headers=headers)
    return res.json()["resModel"]  # 返回任务id

def test_start_task(get_headers_json,taskId1):
    """
    开始任务
    :param get_headers_json:
    :param taskId1:
    :return:
    """
    url = read_url(12)
    headers = get_headers_json
    json = {"content": "自动化创建的施工任务今日开始", "imgList": [], "taskId": taskId1, "receiveUserIdList": [],"receiveTeamIdList": []}
    r = method.HttpRequest()
    r.run_method(url=url, method="POST", json=json, headers=headers)

def test_finish_task(get_headers_json,taskId1):
    """
    通过发布动态关联任务，100%触发完成任务
    :param get_headers_json:
    :param taskId1:
    :return:
    """
    url = read_url(1)
    headers = get_headers_json
    json = {"projectId":projectId(),"type":0,"subTypeName":"","taskId":taskId1,"taskProgress":100,"address":"深圳市福田区人民政府附近","nearBy":"深圳市福田区福民路214号","city":"深圳市","content":"测试100%","originalContent":"测试100%","country":"中国","county":"福田区","imgs":[],"videos":[],"fileIdList":[],"latitude":22.52291,"longitude":114.05454,"province":"广东省","receiveUserIdList":[],"receiveTeamIdList":[],"accessableUserIdList":["-1"],"accessableTeamIdList":["-1"],"weather":"多云","temperature":"30℃","remindAddDto":None,"remindId":""}
    r = method.HttpRequest()
    r.run_method(url=url, method="POST", json=json, headers=headers)

@pytest.fixture(name="actTaskId1",scope='module')
def test_detail_task1(get_headers_json,taskId1):
    """
    查看任务详情，返回任务完成节点id
    :param get_headers_json:
    :param taskId1:
    :return: processInstanceId
    """
    url = read_url(11)
    headers=get_headers_json
    data = {"id":taskId1}
    r = method.HttpRequest()
    res = r.run_method(url=url, method="get", data=data, headers=headers)
    return res.json()["resModel"]["activitiMap"]['currentTaskList'][0]['id']

def test_submitVerify_task(get_headers_json,taskId1,actTaskId1):
    """
    任务提交检验
    :param get_headers_json:
    :param taskId1:
    :param processInstanceId:
    :return:
    """
    url = read_url(10)
    headers = get_headers_json
    json={"content":"提交检验","imgList":[],"taskId":taskId1,"receiveUserIdList":[],"receiveTeamIdList":[],"actTaskId":actTaskId1,"overwriteVerifyUserIdList":[userId()]}
    r = method.HttpRequest()
    r.run_method(url=url, method="POST", json=json, headers=headers)

@pytest.fixture(name="actTaskId2",scope='module')
def test_detail_task2(get_headers_json,taskId1):
    """
    查看任务详情，返回检验节点的id
    :param get_headers_json:
    :param taskId1:
    :return: processInstanceId
    """
    url = read_url(11)
    headers=get_headers_json
    data = {"id":taskId1}
    r = method.HttpRequest()
    res = r.run_method(url=url, method="get", data=data, headers=headers)
    return res.json()["resModel"]["activitiMap"]['currentTaskList'][0]['id']

def test_signCertificate(get_headers,taskId1,actTaskId2):
    """
    点击合格至签章系统
    :param get_headers_json:
    :param taskId1:
    :param actTaskId:
    :return:
    """
    url = read_url(13)
    headers = get_headers
    data = {"projectId":projectId(),"taskId":taskId1,"actTaskId":actTaskId2}
    r = method.HttpRequest()
    res = r.run_method(url=url, method="POST", data=data, headers=headers)
    return res.json()["resModel"]

if __name__ == '__main__':
    pytest.main(["-v","D:/Pycharm/API_Atuo/Test_cases/test_task1.py"])