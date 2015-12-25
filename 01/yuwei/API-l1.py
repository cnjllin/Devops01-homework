# -*- coding: utf-8 -*-

class AutoLoad(object):
    """
        自动加载类
    """
    def __init__(self, module_name):
        #self.moduledir = 获取模块所在的目录
        self.moduledir = "/python_module"
        self.module = None
        self.module_name = module_name
        self.method = None

    def isValidMethod(self, func=None):
        """
            判断方法是否可用
        """
        self.method = func
        #c = getattr(self.module_name,func)
        #print(hasattr(c,func))
        #autoLoad = AutoLoad()
	#print(hasattr(autoLoad,method))
        method_list = self.method 
	module_list = self.module
        try:
            module_list.method_list
            Hello = AutoLoad(module_list)
            return hasattr(Hello,str(method_list))		
        except:
            return false

    def isValidModule(self):
        """
            判断模块是否可加载
        """
        module_list = str(self.module_name)  #去掉.py的文件名
        try:
            module_check = __import__(module_list)
            print module_check
            result = true
            return self._load_module()
        except:
            print "%s can  load failed"	  %(module_list)
            result = false
            #module = __import__(str(check_module))
            return result

    def getCallMethod(self):
        """
            返回可执行的方法
        """
        method_list = self.method
        if method_list in dir(module_list)
            print "module has %s" %(method_list) 
            return method_list
        else:
            print "module has no %s"	  %(method_list)
            return none
		
	 #if 这个模块有这个方法，
	 #	返回这个方法
	 #    return none

    def _load_module(self):
        """
            加载模块
        """
		
        ret = False
        for filename in (ls self.moduledir):
	    #if filename 以.py结尾
            if os.path.splitext(os.path.basename(filename))[1] == ".py":
	    #module_name = filename去掉.py
                module_name = os.path.splitext(os.path.basename(filename))[0]
                if module_name == self.module_name:
                    fp, pathname, desc = imp.find_module(module_name, [self.moduleDIR])
                    if not fp:
                        continue
                        try:
                            self.module = imp.load_module(module_name, fp, pathname, desc)
                            ret = True
                         except: 
                            fp.close()
                            break
        return ret	

class Response(object):
    """
        定义一个response对象
    """
    def __init__(self):
        self.data = None            # 返回的数据
        self.errorCode = 0          # 错误码
        self.errorMessage = None    # 错误信息



class JsonRpc(object):

    def execute(self,id,data):
        """
            执行指定的方法
            返回执行后的结果
        """
        #验证id
        #验证json -> validate()
        data = self.data
        json_str = json.load(data)
	#json_str = json.dumps(data)
        if data[id] is None:
            result = false
	else:	
            #validate()
	    if validate(json_str) is True:        
                callMethod(module, func, params, auth)
                result = true
            else:
                result = false
	
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
        at.isValidModule()
        at.isValidMethod()
        #if at.result == 'false':
        if at.isValidModule() == 'false':
	
        #验证模块是否可加载
        #    false
            response.errorcode = "-100"
            response.errorMessage = "模块不存在"
            return false
        #验证函数是否可调用
	
        if at.isValidMethod() == 'false':
            response.errorcode = "-200"
            response.errorMessage = "函数不存在"
            return false

        flag = requiresAuthentication()  # 判断该操作是否需要验证  true: 需要

	if not flag and auth is not None:
	    return false

        #(需要进行验证)
        if flag: 
            if token is None:
                return false
            else:
                if auth is None:
                    response.errorcode = "-300"
                    response.errorMessage = "没有权限"
                    return false:

        try:
            called = at.getCallMethod()
            #如果 called 可以执行
            if called is not None:
                response.data = called(**params)
                #处理返回结果
                return response.data
            else:
                response.errorcode = "-400"
                response.errorMessage = "函数不存在"
        except:
            response.errorcode = "-500"
	    response.errormsg = "函数执行异常"	
            return false
        return response
	


    def requiresAuthentication(self, module, func):
        """
            判断需要执行的API是否需要验证
        """
        if module == "user" and func == "login":
            response.errorcode = "-600"
            response.errormsg = "无需认证"	
            return False
	
        return True

	
    def validate(self,json_str):
        """
            验证json，以及json传参
        """
            jsonrpc = json_str[jsonrpc]
            method = json_str[method]
            params = json_str[params]
		
            if jsonrpc <> "1.0":
                response.errorcode = "-700"
                response.errormsg = "版本错误"	
                jsonError()
                return false

            if  method not in dir(self.module):
                response.errorcode = "-800"
                response.errormsg = "函数错误"	
                jsonError()
                return false			
			
            if params is None:
                response.errorcode = "-800"
                response.errormsg = "函数错误"	
                jsonError()
                return false		
		
        return True
	    
    def jsonError(self, id, errno, data=None):
        """
            格式化处理错误，转为json格式
        """
        _error = True
        format_error = {
            'jsonrpc': VERSION,
            'error' : data,
            'id': id,
            'errno': errno,
        }
        self.response = json.dumps(format_error)

    def processResult(self, response):
        """
            处理执行后返回的结果
        """
        if response.errorCode != '0':
            errno = response.errorCode
            jsonError()
        else:
            formatResp = {
                "jsonrpc": VERSION,
                "result": response.data,
                "id": json.id
            }
            self.response = json.dumps(formatResp)
        return self.response
 
    def isError(self):
        """
            返回是否有错误
        """
        if self.response is None:
            return false
		
			


