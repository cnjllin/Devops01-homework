#coding:utf-8
#/usr/bin/env python
import os,json

class AutoLoad(object):
    """
       自动加载类
    """
    def __init__(self,module_name):
        self.moduledir = DIR                        ##(模块保存的目录)
        self.module = None                          ##(模块名，李如idc.get里面，，idc就为self.module)
        self.module_name = module_name              ##(用户传入的模块，如idc.get)
        self.method = None                          ##(方法，如idc.get里面的get) 
    def isValidMethod(self, func=None):
        """
           判断方法是否可用
           判断方法是否可以通过func传进来的方法，结合self.module模块，用hasattr判断，有返回True,无返回false
        """
        self.method = func
        return hasattr(self.module,self.method)
    def isValidModule(self):
        """
           判断模块是否可以加载
           调用下面的加载模块函数
        """
        return self._load_module() ###_下划线表示内部使用变量函数
    def getCallMethod(self):
        """
           返回可执行方法
           通过调用isValidMethod函数，根据返回值看是否有方法，有self.method没有返回none
        """
        if isValidMethod(self, func=None):
            return self.method
        return none
    def _load_module(self):
        """
        加载模块
        
        """
        ret = False
        for filename in (os.system("ls %s" %self.meduledir)):
            if filename.endswith(".py"):
                module_name = filename.split(".")[0]
            if module_name == self.module_name:
                fp,pathname,desc = imp.find_module(module_name,[self.moduleDIR])
                if not fp:
                    continue
                try:
                    self.module = imp.load_module(module_name, fp, pathname, desc)
                    ret = True
                except:      ###这里我理解的是不是有问题，无论如何关闭是不是finnaly会好点
                    fp.close()
                break
        return ret
        
class Response(object):
    """
        定义一个response对象
    """
    def __init__(self):
        self.data = None     ##返回数据
        self.errorCode = 0   ##错误码
        self.errorMessage = None   ##错误信息


class JsonRpc(object):
    
    def execute(self,id):
	"""
	    执行指定的方法
	    返回执行后的结果
            通过执行request方法传入id值确认，执行的次序
	"""
	if id is not None:
	    pass
	if validate():
	    result = callMethod(module, func, params, auth):
	    return result
	else:
	    return self.response
    def callMethod(self, module, func, params, auth):
	"""
	   加载模块
	   验证权限
	   执行方法
	   返回response
	"""
	response = Response()
	at = AutoLoad(module)
	if not at._load_module():
	    response.errorCode = "-1"
	    response.errorMessage = "模块不能加载"
	    return False
	if not at.isValidMethod():
	    response.errorCode = "-2"
            response.errorMessage = "函数不存在"
            return False
	flag = requiresAuthentication()
	if not flag and auth is not None:
	    return False
	if flag:
	    if token is None:
		return False
	    else:
		if auth == 0:
		    response.errorCode = "-3"
		    response.errorMessage = "没有权限"
		    return False
	try:
	    called = at.getCallMethod()
	    if called:
		response.data = called(**params)
		return response.data
	    else:
		response.errorCode = "-4"
		response.errorMessage = "函数不可执行"
	except:
	    response.errorCode = "-5"
	    response.errorMessage = "函数异常"
	    return False

	return response
    def requiresAuthentication(self, module, func): 
	"""
	   判断需要执行的API是否需要验证
	"""

    def validate(self,jsondata):
	"""
	   验证json,以及json传参数，遍历json数据并验证
	"""
	jsonrpc = jsondata['jsonrpc']
	method = jsondata['method']
	params = jsondata['params']
	if jsonrpc != '2.0':
	    response.errorCode = '-6'
	    response.errorMessage = "rpc版本问题"
	    jsonError()
	    return False
	if method not in self.module_name:
	    response.errorCode = '-7'
            response.errorMessage = "验证模块有问题"
            jsonError()
            return False
	if len(params) = 0:
	    response.errorCode = '-8'                                                                             
            response.errorMessage = "参数未传递"
            jsonError()                                                                                           
            return False
 
	return True
    def jsonError(self,id,errno,data=None):
	"""
	   格式化错误输出信息
	"""
	format_error = {
	     "jsonrpc":VERSION,
	     "error":data,
	     "id":id,
	     "errno":errno
        }
	self.response = json.dumps(format_error)
    def processResult(self,response):
	"""
	   格式化正确的结果
	"""
	if response.errorCode != 0:
	    errno = response.errorCode
	    jsonError()
	else:
	    formatResp = { 
                "jsonrpc": VERSION,			
                "result": response.data,
	        "id": json.id	
 	        }		
	self.response = json.dumps(formatResp)
    def isError(self):
	"""
	   返回是否有错误
	"""

