#!/usr/bin/env python
# coding:utf-8

from __future__ import unicode_literals
from flask import render_template, request


from . import main
import requests
import json

@main.route("/resource/index", methods=['GET'])
def resource_index():
    return render_template("resource/index.html")


@main.route('/resource/idc', methods=['GET'])
def resource_idc():
    return render_template("resource/server_add_idc.html")


@main.route('/resource/server_add', methods=['GET'])
def resource_server_add():
    #获取idc信息
    idc_info = api_action("idc.get", {"output": ['name', 'id']})
    status = api_action("status.get", {"output": ['id', 'name']})


    return render_template("resource/server_add.html",
                          idc_info=idc_info,
                          status=status)

"""
    添加IDC页面
"""


@main.route('/resource/server_idc_add', methods=['GET'])
def resource_server_idc_add():
    return render_template("resource/server_add_idc.html")


"""
    执行IDC添加
"""

@main.route('/resource/server_idc_doadd', methods=['POST'])
def resource_server_idc_doadd():
    #print request.form
    #data = request.get_json()
    #print data
    ret = api_action("idc.create", dict(request.form))
    print ret

    if str(ret).isdigit():
        return "操作成功"
    else:
        return "操作失败"
    #return render_template("resource/server_add_idc.html")


"""
    添加服务器状态
"""

@main.route('/resource/server_status_add', methods=['GET'])
def resource_server_status_add():
    return render_template("resource/server_add_status.html")


"""
    执行服务器状态添加
"""
@main.route('/resource/server_status_doadd', methods=['POST'])
def resource_server_status_doadd():
    #print request.form
    #data = request.get_json()
    #print data
    ret = api_action("status.create", dict(request.form))
    print ret

    if str(ret).isdigit():
        return "操作成功"
    else:
        return "操作失败"
    #return render_template("resource/server_add_idc.html")




def api_action(action, params):

    url = "http://127.0.0.1:5000/api"
    headers = {"Content-type":"application/json"}

    #create cabinet app/test/test_add_cabin.py
    data = {
        'jsonrpc': 2.0,
        'method': action,
        'id': 1,
        'auth': None,
        'params': params
    }
    r = requests.post(url,headers = headers,json=json.dumps(data))
    if str(r.status_code) == "200":
        ret = json.loads(r.content)
                                  
    if ret.get('result', None):
        return ret['result'] 
    else:
        return ret['error']

    print r.status_code
    print r.content
    



