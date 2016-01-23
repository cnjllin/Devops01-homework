#!/usr/bin/python
#coding:utf-8

import requests
import json 

url = "http://127.0.0.1:5000/api"
headers = {"Content-type":"application/json"}
#create
'''
data = {
    'jsonrpc': '2.0',
    'method':'idc.create',
    'id':1,
    'auth':None,
    'params':{
        "name": "yz2",
        "idc_name": "北京亦庄机房2",
        "address": "北京亦庄",
        "phone": "13512345678",
        "email": "rock@51reboot.com",
        "user_interface": "panda",
        "user_phone": "13643254672",
        "rel_cabinet_num": 30,
        "pact_cabinet_num": 35
#        "test": "test"                                                                                                                                                                               
    }
}
'''
#get
'''
data = {
    'jsonrpc': 2.0,
    'method': 'idc.get',
    'id': 1,
    'auth': None,
    'params': {
              "output": [ 'email','phone' ]
              }
}
'''
'''
#update
data = {
    'jsonrpc': 2.0,
    'method': 'idc.update',
    'id': 1,
    'auth': None,
    'params': {
              "data":{
                    "email": "panda@51reboot.com"
                     },
              "where":{
                     "id": 1
                      }
              }
}
'''

'''
#Status
data = {
    'jsonrpc': 2.0,
    'method': 'status.create',
    'id': 1,
    'auth': None,
    'params': {
              "name": "线上4a",
    }
}
'''
'''
#Status
data = {
    'jsonrpc': 2.0,
    'method': 'status.get',
    'id': 1,
    'auth': None,
    'params': {
              
    }
}
'''
'''
#update
data = {
    'jsonrpc': 2.0,
    'method': 'status.update',
    'id': 1,
    'auth': None,
    'params': {
              "data":{
                    "name": "cccb"
                     },
              "where":{
                     "id": 3
                      }
              }
}
'''

# 缩减测试
#Status
'''
data = {
    'jsonrpc': 2.0,
    'method': 'status.create',
    'id': 1,
    'auth': None,
    'params': {
              "name": "测试",
    }
}
'''

'''
data = {
    'jsonrpc': '2.0',
    'method':'idc.create',
    'id':1,
    'auth':None,
    'params':{
        "name": "jxq",
        "idc_name": "酒仙桥",
        "address": "北京酒仙桥",
        "phone": "13512345678",
        "email": "rock@51reboot.com",
        "user_interface": "panda",
        "user_phone": "13643254672",
        "rel_cabinet_num": 30,
        "pact_cabinet_num": 40
#        "test": "test"                                                                                                                                                                               
    }
}
'''
#get
'''
data = {
    'jsonrpc': 2.0,
    'method': 'idc.get',
    'id': 1,
    'auth': None,
    'params': {
              "output": [ 'email','phone' ]
              }
}
'''
'''
#Status
data = {
    'jsonrpc': 2.0,
    'method': 'power.create',
    'id': 1,
    'auth': None,
    'params': {
              "server_power": "480",
    }
}
'''

data = {
    'jsonrpc': 2.0,
    'method': 'cabinet.update',
    'id': 1,
    'auth': None,
    'params': {
              "data": {
                    "power": "160",
              },
              "where": { "id": 3 }
     }
}


#header
#header
#header
#header
#header
r = requests.post(url,headers = headers,json=json.dumps(data))
#no header
#r = requests.post(url,json=json.dumps(data))
print r.status_code
#print r.content
ret = json.loads(r.content)
print ret

