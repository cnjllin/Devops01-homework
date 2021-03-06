# coding:utf-8
__author__ = 'reboot'
import os
import imp
import logging

"""
    1 确定目录，modules
    2 列出目录下的所有文件
    3 循环所有的文件名，找出.py结尾的文件名
    4 需要加载的模块名与当前循环的文件名是否一样
    5 加载这个模块
    6 判断这个模块有没有指定的方法
    7 返回这个方法
    8 执行这个方法
"""
# -*- coding: utf-8 -*-
import logging
import math

logger = logging.getLogger()
#set loghandler
file = logging.FileHandler("base.log")
logger.addHandler(file)
#set formater
#formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")




file.setFormatter(formatter) 
#set log level
logger.setLevel(logging.NOTSET)



#for i in range(0,10):
#	logger.info(str(i))



class AutoLoad():
    def __init__(self, module_name):
        DIR = os.path.abspath(os.path.dirname(__file__))
        self.moduleDir = os.path.join(os.path.dirname(DIR), "modules")
        self.module_name = module_name
        self.method = None

    def isValidModule(self):
        """
            判断模块是否可加载
        """
        return self._load_module()

    def isValidMethod(self, func=None):
        """
            判断方法是否可用
        """
        self.method = func
        return hasattr(self.module, self.method)

    def getCallMethod(self):
        if hasattr(self.module, self.method):
            return getattr(self.module, self.method)
        return None

    def _load_module(self):
        ret = False
        for filename in os.listdir(self.moduleDir):
            if filename.endswith('.py'):
                module_name = filename.rstrip(".py")
                if self.module_name == module_name:
                    fp, pathname, desc = imp.find_module(module_name, [self.moduleDir])
                    if not fp:
                        continue
                    try:
                        self.module = imp.load_module(module_name, fp, pathname, desc)
                        ret = True
                    finally:
                        fp.close()
                    break
                else:
                    print "没有找到"
                    logger.info("没有找到")
###
        logger.info("_load_module")
        logger.info(ret)
        return ret

class Response(object):
    """
        定一个response 象
    """
    def __init__(self):
        self.data = None            # 返回的数据
        self.errorCode = 0          # 错误码
        self.errorMessage = None    # 错误信息

class JsonRpc(object):
    def __init__(self, jsonData):
        self.VERSION = "2.0"
        self._error = True
        self.jsonData = jsonData
        self._response = {}

    def execute(self):
        if not self.jsonData.get('id', None):
            self.jsonData['id'] = None

        if self.validate():
            params = self.jsonData.get('params', None)
            auth = self.jsonData.get('auth', None)
            module, func = self.jsonData.get("method", "").split(".")
            ret = self.callMethod(module, func, params, auth)
            self.processResult(ret)
###
        logger.info("execute self._response")
        logger.info(self._response)
        return self._response

    def processResult(self, response):
        if response.errorCode != 0:
            self.jsonError(self.jsonData.get('id'), response.errorCode, response.errorMessage)
        else:
            self._response = {
                "jsonrpc": self.VERSION,
                "result": response.data,
                "id": self.jsonData.get('id')
            }

###
        logger.info("processResult self._response")
        logger.info(self._response)

    def callMethod(self, module, func, params, auth):
        module_name = module.lower()
        func = func.lower()
        response = Response()
        autoload = AutoLoad(module_name)

        if not autoload.isValidModule():
            response.errorCode = 106
            response.errorMessage = "指定的module不存在"
            return response

        if not autoload.isValidMethod(func):
            response.errorCode = 107
            response.errorMessage = "{}下没有{}该方法".format(module_name, func)
            return response

        flag = self.requireAuthentication(module_name, func)
        if flag:
            if auth is None:
                response.errorCode = 108
                response.errorMessage = "该操作需要提供token"
                return response
            else:
                pass
        try:
            called = autoload.getCallMethod()
            if callable(called):
                response.data = called(**params)
            else:
                response.errorCode = 109
                response.errorMessage = "{}.{} 不能被调用".format(module_name, func)
        except Exception, e:
            response.errorCode = -1
            response.errorMessage = e.message

###         
            logger.error(e)
            return response

###
        logger.info("callMethod")
        logger.info(response)   
        return response

    def requireAuthentication(self, module, func):
        if module == "user" and func == "login":
            return False
        if module == "reboot":
            return False
        return True

    def validate(self):
        if not self.jsonData.get('jsonrpc', None):
            self.jsonError(self.jsonData.get('id', 0), 101, "参数jsonrpc没有传")
            return False
        if str(self.jsonData.get("jsonrpc")) != self.VERSION:
            self.jsonError(self.jsonData.get('id', 0), 101, "参数jsonrpc的版本不正确，应该为:{}".format(self.VERSION))
            return False
        if not self.jsonData.get('method',None):
            self.jsonError(self.jsonData.get('id', 0), 102, "参数method没有传")
            return False
        if "." not in self.jsonData.get('method'):
            self.jsonError(self.jsonData.get('id', 0), 104, "参数method 格式不正确")
            return False
        if self.jsonData.get("params", None) is None:
            self.jsonError(self.jsonData.get('id', 0), 103, "params没有传")
            return False
        if not isinstance(self.jsonData.get("params"), dict):
            self.jsonError(self.jsonData.get('id', 0), 105, "params应该为dict")
            return False
        return True

    def jsonError(self, id, errno, errmsg):
        self._error = True
        format_err = {
            "jsonrpc": self.VERSION,
            "error": errmsg,
            "errno": errno,
            "id": id,
        }
        self._response = format_err

"""
    101  jsonrpc版本，或没有个参数
    102, "参数method没有传"
    103, "params没有传"
    104, "参数method 格式不正确"
    105, "params应该为dict"
    106 "指定的module不存在"
    107  {}下没有{}该方法
    108 该操作需要提供token
    109  不能调用
    -1   api里有except
"""

if __name__ == "__main__":
    data = {
        "jsonrpc": 2.0,
        'method': "reboot.get",
        "params": {"aa":"bb"},
    }
    jrpc = JsonRpc(data)
    ret = jrpc.execute()
    print ret

