#!/usr/bin/env python
#coding:utf8

"""
有几处还是没有看太懂
找个时间在练习练习吧
"""


import os
import imp


class AutoLoad(object):

    def __init__(self, module_name):
        DIR = os.path.dirname(os.path.abspath(__file__))
        self.module_dir = os.path.join(os.path.dirname(DIR), "modules")
        self.module_name = module_name

    def isValidMethod(self, func=None):
        self.method = func
        return hasattr(self.module, self.method)

    def isValidModule(self):
        return self._load_module()

    def getCallMethod(self):
        if hasattr(self.module, self.method):
            return getattr(self.module, self.method)
        return None

    def _load_module(self):
        ret = False
        for filename in os.listdir(self.module_dir):
            if filename.endswith(".py"):
                #module_name = filename.split('.')[0]
                module_name = filename.rstrip(".py")
                if module_name == self.module_name:
                    fp, filename, desc = imp.find_module(module_name, [self.module_dir])
                    if not fp:
                        continue
                    try:
                        self.module = imp.load_module(module_name, fp, filename, desc)
                        ret = True
                    except Exception,e:
                        fp.close()
                    break
        return ret


class Response(object):
    
    def __init__(self):
        self.data = None
        self.errorCode = 0
        self.errorMessage = None

class JsonRpc(object):
    
    def __init__(self, jsonData):
        self.VERSION = "2.0"
        self.jsonData = jsonData
        self._errorCode = True
        self._response = {}

    def execute(self):
        if not self.jsonData.get("id",None):
            self.jsonData["id"] = None

        if self.validate():
            params = self.jsonData.get("params", None)
            auth = self.jsonData.get("auth", None)
            module, func = self.jsonData.get("method","").split(".")
            ret = self.callMethod(module, func, params, auth)
            self.processResult(ret)
        return self._response

    def processResult(self, response):
        if response.errorCode != 0:
            self.jsonError(self.jsonData.get("id"), response.errorCode, response.errorMessage)
        else:
            self._response = {
                "jsonrpc" : self.VERSION,
                "result" : response.data,
                "id" : self.jsonData.get("id")
                }

    def callMethod(self, module, func, params, auth):
        module_name = module.lower()
        func = func.lower()

        response = Response()
        autoload = AutoLoad(module_name)

        if not autoload.isValidModule():
            response.error = 111
            response.Message = "指定的模块不存在"
            return response

        if not autoload.isValidMethod(func):
            response.error = 112
            response.Message = "{}下没有{}方法".format(module_name, func)
            return response

        flat = self.requireAuthentication(module_name, func)
        if flat:
            if auth is None:
                response.error = 113
                response.Message = "该操作需要提供token."
                return response
            else:
                pass
        try:
            called = autoload.getCallMethod()
            if callable(called):
                response.data = called(**params)
            else:
                response.error = 114
                response.Message = "{}.{}不能被调用".format(module_name, func)
        except Exception,e:
            print 'e',e
            response.error = -1
            response.Message = e.message

        return response

    def requireAuthentication(self, module, func):

        #desc: 
        #user.login
        #
        #modules/user.py 
        #    def login():
        #        pass
        #如果return False,表示不验证，直接通过.
        #否则return True,表示需要验证.

        if module == "user" and func == "login":
            return False
        if module == "reboot":
            return False
        return True
        
            
    def validate(self):
        if not self.jsonData.get("jsonrpc",None):
            self.jsonError(self.jsonData.get("id",0), 101,"jsonrpc没有传.")
            return False
        if str(self.jsonData.get("jsonrpc")) != self.VERSION:
            self.jsonError(self.jsonData.get("id",0), 102, "jsonrpc版本必须为{}".format(self.VERSION))
            return False
        if not self.jsonData.get("method",None):
            self.jsonError(self.jsonData.get("method",0), 103,"参数method没有传.")
            return False
        if self.jsonData.get("params",None) is None:
            self.jsonError(self.jsonData.get("params",0), 104,"参数method没有传.")
            return False
        if not isinstance(self.jsonData.get("params", None),dict):
            self.jsonError(self.jsonData.get("params",0), 105,"参数method必须为字典类型 ")
            return False
        return True
            

    def jsonError(self, id, errno, errmsg):
        self._error = True
        format_err = {
            "jsonrpc" : self.VERSION,
            "error" : errmsg,
            "errno" : errno,
            "id" : id
            }
        self._response = format_error


if __name__ == "__main__":
    #at = AutoLoad('reboot')
    #at.isValidModule()

    localinfo = {
        "jsonrpc" : 2.0,
        "method" : "reboot.get",
        "params" : {"name":"zhengys"}
    }
    jrpc = JsonRpc(localinfo)
    ret = jrpc.execute()
    print ret
