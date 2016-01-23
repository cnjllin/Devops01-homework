#!/usr/bin/python
#coding:utf-8

import requests
import json 

url = "http://127.0.0.1:5000/api"
headers = {"Content-type":"application/json"}


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

#create cabinet
data = {
    'jsonrpc': 2.0,
    'method': 'cabinet.create',
    'id': 1,
    'auth': None,
    'params': {
              "name": "A11-32",
              "idc_id": "jxq",
              "power": "460",
    }
}

#update cabinet
'''
data = {
    'jsonrpc': 2.0,
    'method': 'cabinet.create',
    'id': 1,
    'auth': None,
    'params': {
              "name": "A11-26",
              "idc_id": "jxq",
              "power": "400",
    }
}
'''
'''
#update
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
'''
'''
data = {
    'jsonrpc': 2.0,
    'method': 'cabinet.get',
    'id': 1,
    'auth': None,
    'params': {
#              "output": [ 'id','name','idc_name','power' ]
              }
}
'''



#create
r = requests.post(url,headers = headers,json=json.dumps(data))
#no header
#r = requests.post(url,json=json.dumps(data))
print r.status_code
#print r.content
ret = json.loads(r.content)
print ret

