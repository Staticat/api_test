import requests
import json
import pprint
from Common import assert_
from Config import read_config
from logs.log import log1
from Params import read_yml

def get_url(num):
    test_url  = read_config.read_config("基础信息",'url')
    url =  '/'.join([test_url,read_yml.read_url(num,'url')])
    return url
    # return '/'.join([test_url,url])

class HttpRequest(object):
    """
    请求方法
    """
    def get_method(self,url,data,headers=None):
        res = requests.get(url,data,headers=headers)
        assert_.assert_(res)
        return res

    def post_method(self,url,data=None,headers=None,json=None):
        res = requests.post(url, data=data,json=json,headers=headers)
        assert_.assert_(res)
        return res

    def del_method(self,url,headers=None,params=None):
        res = requests.delete(url,params=params,headers=headers)
        # assert_.assert_(res)
        return res

    def run_method(self,method,url,data=None,headers=None,json=None,params=None):
        res = None #去除局部变量的警告
        if method=='get' or method=='GET':
            res = self.get_method(url,data,headers)
        elif method=='post' or method=='POST':
            res = self.post_method(url,data,headers,json)
        elif method=='del' or method=='DEL':
            res = self.del_method(url,headers,params)
        return res
        # return pprint.PrettyPrinter(indent=2).pprint(res)
        # return json.dumps(res,indent=4)
        # return json.dumps(res, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ':'))
