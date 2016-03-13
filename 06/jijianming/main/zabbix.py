#!/usr/bin/env python
#-*- coding:utf-8 _*_

from __future__ import unicode_literals
from app.common import api_action
from app.models import db,Server,ZbHost
from flask import render_template, request
import json
from . import main

@main.route('/resources/groups/zabbix_action',methods=['GET'])
def zabbox():
    return render_template('groups/groups_zabbix.html')



'''
获取zabbix所有host groups
'''
@main.route('/monitor/ajax/get_zabbix_host_groups',methods=['POST'])
def get_zabbix_host_groups():
    from app.common.zabbix import zabbix_server
    host_groups = zabbix_server.get_hostgroup()
    return json.dumps(host_groups)

@main.route('/monitor/ajax/get_zabbix_data_by_group',methods=['POST'])
def get_zabbix_data_by_group():
    from app.common.zabbix import get_zabbix_data,init
    init()
    params = dict(request.form)
    hosts = api_action('server.get',
        {
        'output':['id'],
        'where':{
            'server_purpose':params['server_purpose'][0],
            'service_id':params['service_id'][0]}
        })
    ret = get_zabbix_data(hosts)
    return json.dumps(ret)

'''
    给主机绑定指定模版
'''
@main.route('/monitor/ajax/link_zabbix_template',methods=['POST'])
def link_zabbix_template():
    print 'link--------'
    data = dict(request.form)
    from app.common.zabbix import link_template
    hostids = data['hostids'][0].split(',')
    templateids = data['template_ids'][0].split(',')
    ret_data = link_template(hostids,templateids)
    error = None
    for r in ret_data:
        try:
            hostids.remove(r['hostids'][0])
        except Exception,e:
            error = e.message
    print ret_data
    if not hostids:
        return '1'
    else:
        return json.dumps(ret_data)
    return '500'