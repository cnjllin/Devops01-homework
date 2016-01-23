#!/usr/bin/env python
# coding:utf-8
from __future__ import unicode_literals
from flask import request
from . import main
import json
from app.core.base import JsonRpc
import logging


@main.route('/', methods=['GET','POST'])
def index():
    return 'index'

@main.route('/api', methods=['GET','POST'])
def api():
    #logging.DEBUG( "API 被调用")
    allowed_content = {
        'application/json-rpc':"json-rpc",
        'application/json':"json-rpc",
    }#定义2种允许的请求方式
    #print  request.content_type
    #logging.debug(request.content_type)
    #return  "aaa"
    #print request.content_type
    #print request.get_json()
    if allowed_content.get(request.content_type, None):
        jsonData =  json.loads(request.get_json())
        jsonrpc = JsonRpc(jsonData)
        ret = jsonrpc.execute()
        return json.dumps(ret)
    else:
        return "404",404
