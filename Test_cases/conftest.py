import pytest
from Test_cases.test_login import test_login
import os
from Config.read_config import appId

@pytest.fixture(scope='module')
def get_token():
    '''
    获取并返回token
    :return:
    '''
    token=test_login()
    return token

@pytest.fixture(scope='module')
def get_headers(get_token):
    """
    带token，默认Content-Type的headers
    :param get_token:
    :return:
    """
    headers = {"Accept": "*/*", "appId": appId(),"token":get_token}
    return headers

@pytest.fixture(scope='module')
def get_headers_json(get_token):
    """
    带token，"Content-Type":"application/json"
    :param get_token:
    :return:
    """
    headers = {"Accept": "*/*", "appId":appId(),"token":get_token,"Content-Type":"application/json"}
    return headers

@pytest.fixture(scope='module')
def get_cwd():
    path = os.path.dirname(os.path.abspath(__file__))
    return path


