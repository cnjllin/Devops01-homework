#!/usr/bin/env python
#coding=utf8
#api伪代码
import os,imp

class AutoLoad(object):
    def __init__(self, module_name):
        """自动加载类"""
        self.moduledir = os.path.dirname(url)
        self.module = None
        self. module_name = module_name
        self.mothod = None

    def isValidMethod(self, func=None):
        """判断方法是否可用"""
        self.method = func
        return hasattr(AutoLoad("module_name"), "func")

    def isValidModule(self):
        """判断模块是否可加载"""
        return self._load_module()

    def getCallMethod(self):
        """返回可执行方法,如果没有返回None"""
        return getattr(AutoLoad("module_name"), "method", None)

    def _load_module(self):
        """加载模块"""
        ret = False
        for filename in (os.system("ls %s" % self.moduledir)):
            if filename[-3:] == ".py":
                module_name = filename[:-3]
            if module_name ==self.module_name:
                fp, pathname, desc = imp.find_module(module_name, [self.moduledir])
                if not fp:
                    continue
                try:
                    self.module = imp.load_module(module_name, fp, pathname, desc)
                    ret = True
                except:
                    pass
                finally:
                    fp.close()
                    break
        return ret


class Response(object):
    """定义一个response对象"""
    def __init__(self):
        self.data = None #返回的数据
        self.errorCode = 0 #错误码
        self.errorMessage = None # 错误信息

class JsonRpc(object):
    def execute(self):
        """执行指定方法，返回执行后结果"""
        #if id and json -> validate():
            #idc.get -> callMethod()
            #处理返回结果
        #else:
            #return self.response

    def callMethod(self, module, func, params, auth):
        """加载模块，验证权限，执行方法， 返回response"""
        response = Response()
        at = AutoLoad(module)
        if not at.isValidModule():
            response.errorCode = -100
            response.errorMessage = "模块不存在"
            return False

        if not at.isValidMethod(func):
            print "方法不可调用"
            return False

        flag = requiresAuthentication() #判断操作是否需要验证

        #需要验证
        if flag:
            if not token:
                return false
        else:
        #是否有权限操作: idc.get ?
            #  if 没有权限:return False

        try:
            called = func
            if called可执行:
                return response.data = called(**params)
            else:
                errorcode = 111
                errormsg = "called 不可执行"
        except:
            response.errorCode = 123
            response.errorMessage = "找不到该方法"
            return False

        return response

    def requiresAuthentication(self, module, func):
        """判断需要执行的API是否需要验证"""
        if module == "user" and func == "login":
            return False
        return True

    def validate(self):
        """验证json，以及json传参"""
        #if 验证 jsonrpc, 验证版本
        #else:
            #jsonError()
            # return false
        #验证method, idc.get
            #jsonError()
            # return false
        #验证params是否传
            #jsonError()
            # return false
        return True

    def jsonError(self, id, errno, data=None):
        """处理json错误"""
        _error = True
        format_error = {'jsonrpc':VERSION, 'error':data, 'id':id, 'errno':errno}
        self.response = format_error

    def processResult(self, response):
        """处理执行后返回的结果"""
        if response.errorCode != 0:
            errno = response.errorCode
            jsonError()
        else:
            formatResp = {"jsonrpc":VERSION, "result":response.data, "id":jsonid}
            self.response = formatResp

    def isError(self):
        """返回是否有错?"""










