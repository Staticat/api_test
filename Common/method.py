import requests
import json
from Common import assert_

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
        assert_.assert_(res)
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
