#!/usr/bin/env python
#_*_coding:utf-8_*_
import os
import psutil
import socket
'''
mem = psutil.virtual_memory()
cpu = psutil.cpu_count(logical=False)
print '主机名:%s'% socket.gethostname()
for i in psutil.disk_partitions():
    print "盘符:%s 挂载点:%s 使用率:%s%s" % (i[0],i[1],psutil.disk_usage(i[1])[3],'%')
print 'CPU个数:%s个'% cpu
print '总内存:%sM'% int(mem.total/1024/1024)
print '使用内存:%sM'% int(mem.used/1024/1024)
print '剩余内存:%sM'% int(mem.free/1024/1024)
# sudo dmidecode -t 1|egrep "Manufa|Pro|Serial Number"
#    Manufacturer: VMware, Inc.
#    Product Name: VMware Virtual Platform
#    Serial Number: VMware-56 4d eb 22 c6 4c 63 f8-a1 6a 91 49 6d f5 fd 5f
print '服务器型号:%s'% os.popen('sudo dmidecode -t 1|egrep Manufa|cut -d: -f2').read().strip()
print '服务器厂商:%s'% os.popen('sudo dmidecode -t 1|egrep Pro|cut -d: -f2').read().strip()
print 'SN号:%s'% os.popen('sudo dmidecode -t 1|egrep Serial|cut -d: -f2').read().strip()
'''
def system_info():
    hostname = socket.gethostname()
    mem = psutil.virtual_memory()
    mem_total = int(mem.total/1024/1024)
    mem_used = int(mem.used/1024/1024)
    mem_free = int(mem.free/1024/1024)
    cpu_num = psutil.cpu_count(logical=False)
    system_model = os.popen('sudo dmidecode -t 1|egrep Manufa|cut -d: -f2').read().strip()
    sys_info = os.popen('sudo dmidecode -t 1|egrep Pro|cut -d: -f2').read().strip()
    sn = os.popen('sudo dmidecode -t 1|egrep Serial|cut -d: -f2').read().strip()
    print  '主机名:%s,\nCPU个数:%s个,\n总内存:%sM,\n使用内存:%sM,\n剩余内存:%sM,\n服务器型号:%s,\n服务器厂商:%s,\nSN号:%s'% (hostname,cpu_num,mem_total,mem_used,mem_free,system_model,sys_info,sn)
    for i in psutil.disk_partitions():
        print  "盘符:%s 挂载点:%s 使用率:%s%s" % (i[0],i[1],psutil.disk_usage(i[1])[3],'%')
    
system_info()
