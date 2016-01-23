#!/usr/bin/python
#coding:utf-8

import requests
import json 

url = "http://127.0.0.1:5000/api"
headers = {"Content-type":"application/json"}
'''
data = {
    'jsonrpc': '2.0',
    'method':'idc.create',
    'id':1,
    'auth':None,
    'params':{
        "name": "yz",
        "idc_name": "北京亦庄机房",
        "address": "北京亦庄",
        "phone": "13512345678",
        "email": "rock@51reboot.com",
        "user_interface": "panda",
        "user_phone": "13643254672",
        "rel_cabinet_num": 30,
        "pact_cabinet_num": 35,
        "test": "test"                                                                                                                                                                               
    }
}
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

#header
r = requests.post(url,headers = headers,json=json.dumps(data))
#no header
#r = requests.post(url,json=json.dumps(data))
print r.status_code
print r.content

