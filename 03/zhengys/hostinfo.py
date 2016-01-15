#!/usr/bin/env python
#coding:utf8
#Author:zhengys
#Finsh:2016-01-15

"""
没有更多的时间去做作业，也就趁着周五闲的时候写了几乎一天。剩余的作业暂时还没有写。
"""

import psutil
from subprocess import Popen,PIPE
import shlex
import re
import platform
import json

class HostInfo(object):

    def __init__(self):
        pass

    def get_ip(self):
        ips = {}
        inetnames = psutil.net_if_addrs().keys()
        inetnames.remove("lo")
        for inet in inetnames:
            addr = psutil.net_if_addrs()[str(inet)][0].address 
            ips[str(inet)] = addr
        return ips

    def get_cpu(self):
        return psutil.cpu_count()

    def get_memory(self):
        memorys = {}
        token = psutil.virtual_memory()
        memorys["total"] = psutil.virtual_memory().total
        memorys["used"] = psutil.virtual_memory().used
        memorys["free"] = psutil.virtual_memory().free
        memorys["percent"] = psutil.virtual_memory().percent

        return memorys

    def get_disk(self):
        partitions = [ i.mountpoint for i in psutil.disk_partitions() ]
        disks = {}
        for i in partitions:
            token = psutil.disk_usage('%s' % i)
            disks[i] = {"total" : token.total, "used" : token.used, "free" : token.free}
        return disks


    def get_hardinfo(self):

        try:
            cmd = "dmidecode"
            P = Popen(shlex.split(cmd), stdout=PIPE, stderr=PIPE) 
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

        except Exception, e:
            print "please execute install command 'yum install dmidecode -y' on the system of linux."
            return False 

    def get_hostname(self):
        return platform.node()

    def get_systemversion(self):
        return " ".join(list(platform.dist()))

    def main(self):
        disk = self.get_disk()
        memorys = self.get_memory()

        FD = FormatDesc()
        memory = FD.formatMem(memorys)
        disk = FD.formatDisk(disk)

        output = {  
            "ip" : self.get_ip(),
            "hostname" : self.get_hostname(),
            "system" : self.get_systemversion(),
            "cpu" : self.get_cpu(),
            "memory" : memory
            }

        if self.get_hardinfo():
            output = dict(output.items() + self.get_hardinfo().items() + disk.items())
            print json.dumps(output, indent=4)

        
class FormatDesc(object):

    def __init__(self):
        self.unit = {"b" : 2**0, "k" : 2**10, "m" : 2**20, "g" : 2**30}

    def formatMem(self, data):
        memory = {}
        for name, num in data.items():
            for k, v in self.unit.items():
                if name != "percent":
                    ret = float(num) / v
                    if ret > 0 and ret <= 1024: 
                        ret = "%.2f%s" % (ret, k)
                        memory[name] = ret
                        break
                else:
                    memory["percent"] = num
        return memory

    def formatDisk(self, data):
        diskinfo = {}
        disk = {}
        for partition, dic in data.items():
            for name, num in dic.items():
                for k, v in self.unit.items():
                    ret = float(num) / v
                    if ret > 0 and ret <= 1024:
                        ret = "%.2f%s" % (ret, k)
                        disk[name] = ret
                        diskinfo[partition] = disk
                        break
        return diskinfo


if __name__ == "__main__":
    HI = HostInfo()
    HI.main()
