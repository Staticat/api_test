from Common import method
from Params import read_yml
import pytest
from Config.read_config import projectId,userId

@pytest.fixture()
def test_add_dynamic(get_headers_json):
    """
    发布动态（带图片/文件/任务）
    :param get_headers_json:
    :return:
    """
    url = method.get_url(1)
    json = read_yml.read_data(1, 'data')
    headers = get_headers_json
    r = method.HttpRequest()
    res = r.run_method(url=url, method="POST", json=json, headers=headers)
    return res.json()["resModel"] #返回动态id

@pytest.fixture()
def test_add_dynamic_remark(get_headers_json,test_add_dynamic):
    """
    动态评论
    :param get_headers_json:
    :return:
    """
    url = method.get_url(2)
    json = {"content":"测试","dynamicId":test_add_dynamic,"projectId":projectId(),"imgs":[]}
    headers = get_headers_json
    r = method.HttpRequest()
    res = r.run_method(url=url, method="POST", json=json, headers=headers)
    return res.json()["resModel"]["id"] #返回评论的id

def test_addRemarkResponse(get_headers_json,test_add_dynamic,test_add_dynamic_remark):
    """
    回复评论
    :param get_headers_json:
    :param test_add_dynamic:
    :param test_add_dynamic_remark:
    :return:
    """
    url = method.get_url(3)
    json = {"content":"测试","dynamicId":test_add_dynamic,"projectId":projectId(),"imgs":[],"remarkId":test_add_dynamic_remark,"responseeUserId":userId()}
    headers = get_headers_json
    r = method.HttpRequest()
    res = r.run_method(url=url, method="POST", json=json, headers=headers)

@pytest.mark.testdel
def test_del_dynamic_remark(get_headers_json,test_add_dynamic,test_add_dynamic_remark):
    """
    删除评论
    :param get_headers_json:
    :param test_add_dynamic:
    :param test_add_dynamic_remark:
    :return:
    """
    url = method.get_url(4)
    params = {"dynamicId":test_add_dynamic,"projectId":projectId(),"remarkId":test_add_dynamic_remark}
    headers = get_headers_json
    r = method.HttpRequest()
    res = r.run_method(url=url, method="del",headers=headers,params=params)
    # return res.text

if __name__ == '__main__':
    pytest.main(["-s","D:/Pycharm/API_Atuo/Test_cases/test_dynamic.py"])
