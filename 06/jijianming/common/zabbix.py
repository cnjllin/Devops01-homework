#!/usr/bin/env python
#-*- coding:utf-8 -*-

from zabbix_client import ZabbixServerProxy
from flask import current_app
from app.models import ZbHost,db,Server
from app.common import api_action

conf = current_app.config

zabbix_url = conf.get('SQLALCHEMY_ZABBIX_API_URL')
zabbix_user = conf.get('SQLALCHEMY_ZABBIX_API_USER')
zabbix_pass = conf.get('SQLALCHEMY_ZABBIX_API_PASS')

class Zabbix():
    def __init__(self):
        self.zb = ZabbixServerProxy(zabbix_url)
        self.zb.user.login(user=zabbix_user,password=zabbix_pass)
    def get_host(self):
        return self.zb.host.get(output=['hostid','host'])

    def get_interface(self,hostids):
        data = self.zb.hostinterface.get(hostids=hostids,output=['hostid','ip'])
        ret = {}
        for d in data:
            ret[d['hostid']] = d['ip']
        return ret
    def get_hostgroup(self):
        return self.zb.hostgroup.get(output=['groupid','name'])

    def create_host(self,params):
        return self.zb.host.create(**params)
    def get_template(self,hostid):
        ret = self.zb.template.get(hostids=hostid,output=['templateid','name'])
        return ret
    def host_link_template(self,hostid,templateids):
        templates = []
        for id in templateids:
            templates.append({'templateid':id})
        ret = self.zb.host.update(hostid=hostid,templates=templates)
        return ret

zabbix_server = Zabbix()
def init():
    #清空cache
    db.session.execute('truncate {0}'.format(ZbHost.__tablename__))
    init_zabbix()
    init_cmdb()

def init_cmdb():
    #取出host(server表中)
    hosts = api_action('server.get')
    #更新到cache表
    for h in hosts:
        data = {'cmdb_hostid':h['id']}
        db.session.query(ZbHost).filter_by(ip=h['inner_ip']).update(data)

    db.session.commit()

def init_zabbix():
    #第一步:取出所有host(ip,host,id)
    zb_hosts = zabbix_server.get_host()
    zb_hosts_interface = zabbix_server.get_interface([z['hostid'] for z in zb_hosts])
    for h in zb_hosts:
        if zb_hosts_interface[h['hostid']] == '127.0.0.1':
            continue
        h['ip'] = zb_hosts_interface[h['hostid']]
        db.session.add(ZbHost(**h))
    db.session.commit()

def get_zabbix_data(hosts):
    '''
    获取zabbix主机的机器和模版信息
    :param hosts:
    :return:
    '''
    ret = []
    zabbix_data = db.session.query(ZbHost).filter(ZbHost.cmdb_hostid.in_([h['id'] for h in hosts])).all()
    db.session.close()

    for zb_host in zabbix_data:
        tmp = {}
        tmp['hostname'] = zb_host.host
        tmp['templates'] = zabbix_server.get_template(zb_host.hostid)
        tmp['hostid'] = zb_host.hostid
        ret.append(tmp)
    return ret
def link_template(hostids,templates):
    ret = []

    for hostid in hostids:
        link_template_ids = [t['templateid'] for t in zabbix_server.get_template(hostid)]
        link_template_ids.extend(templates)
        ret.append(zabbix_server.host_link_template(hostid,link_template_ids))
    return ret
def create_zabbix_host(hostids,groupid):
    #根据传的hostid,去数据库中查询到对应的ip,hostname
    servers = db.session.query(Server).filter(Server.id.in_(hostids)).all()
    ret = []
    for host in servers:
        data = {
            'host':host.hostname,
            'interfaces':[
                {
                    'type':1,
                    'main':1,
                    'useip':1,
                    'ip':host.inner_ip,
                    'dns':'',
                    'port':'10050'
                }
            ],
            'groups':[
                {
                    'groupid':groupid
                }
            ]
        }
        ret.append(zabbix_server.create_host(data))
    return ret


