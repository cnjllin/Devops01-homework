#!/usr/bin/env python
#coding:utf8
#Author:zhengys
#Finsh:2016-01-15
#update:2016-01-17

"""
参考文档：https://pypi.python.org/pypi/psutil
"""

import psutil
from subprocess import Popen,PIPE
import shlex
import re
import platform
import json

unit = {"b" : 2**0, "k" : 2**10, "m" : 2**20, "g" : 2**30}


def get_ip():
    '''
    获取本地除"lo"之外的所有网卡ip地址信息.
    '''
    ips = {}
    inetnames = psutil.net_if_addrs().keys()
    inetnames.remove("lo")
    for inet in inetnames:
        addr = psutil.net_if_addrs()[str(inet)][0].address
        ips[str(inet)] = addr
    return ips

def get_cpu():
    '''
    获取本地物理cpu的个数.
    '''
    return psutil.cpu_count()

def get_memory():
    '''
    获取本地磁盘的总共、使用、剩余空间量
    '''
    memorys = {}
    token = psutil.virtual_memory()
    memorys["total"] = psutil.virtual_memory().total
    memorys["used"] = psutil.virtual_memory().used
    memorys["free"] = psutil.virtual_memory().free
    Mem = formatMem(memorys)
    return Mem

def get_disk():
    '''
    获取本地磁盘各分区的使用总共、使用、剩余空间量.
    '''
    local_all_partitions = [ i.mountpoint for i in psutil.disk_partitions() ]
    disks = {}
    for partitions in local_all_partitions:
        token = psutil.disk_usage('%s' % partitions)
        disks[partitions] = {"total" : token.total, "used" : token.used, "free" : token.free}
    return formatDisk(disks)

def get_hostname():
    '''
    获取本地主机名
    '''
    return platform.node()

def get_system():
    '''
    获取本地操作系统版本号
    ''' 
    return " ".join(list(platform.dist()))

def cmd_ret():
    '''
    获取本地服务器的制造商、产品名称、SN、uuid、出厂日期
    '''
    try:
        cmd = "dmidecode"
        P = Popen(shlex.split(cmd), stdout=PIPE, stderr=PIPE) 
    except Exception, e:
        print "command {} not install".format(cmd)
        return None 

    data = P.stdout.read()
    line = data.split("\n\n")[2]

    Manufacturer = re.findall(r"Manufacturer:\s(.*)", line)[0]
    Product_Name = re.findall(r"Product Name:\s(.*)", line)[0]
    SN = re.findall(r"Serial Number:\s(.*)", line)[0]
    UUID = re.findall(r"UUID:\s(.*)", line)[0]
    production_date = re.findall(r"Release Date:\s(.*)", data)[0]

    format_date = production_date.split("/")
    format_date.reverse()
    production_date_format  = "-".join(format_date)
    
    return {"Manufacturer":Manufacturer,"Product_Name":Product_Name,"SN":SN,"UUID":UUID,"production_date":production_date_format}

def formatMem(data):
    ret_memory = {}
    for name, num in data.items():
        for k, v in unit.items():
            ret = float(num) / v
            if ret > 0 and ret <= 1024:
                ret = "%.2f%s" % (ret, k)
                ret_memory[name] = ret
                break
    return ret_memory

def formatDisk(data):
    ret_diskinfo = {}
    disk = {}
    for partition, dic in data.items():
        for k, v in unit.items():
            for name, num in dic.items():
                ret = float(num) / v
                if ret > 0 and ret <= 1024:
                    format_num = "%.2f %s" % (ret, k)
                    disk[name] = format_num
        ret_diskinfo[partition] = disk
    return ret_diskinfo

def main():
    ips = get_ip()
    cpu = get_cpu()
    memory = get_memory()
    disk = get_disk()
    hostname = get_hostname()
    system = get_system()
    ret = cmd_ret()

    output = {
        "ip" : ips,
        "hostname" : hostname,
        "memory" : memory,
        "cpu" : cpu,
        "disk" : disk,
        "system" : system
        } 
    if ret:
        data = dict(output.items() + ret.items())
        return json.dumps(data, indent=4)
    return None
    
if __name__ == "__main__":
    format_info = main()
    print format_info

