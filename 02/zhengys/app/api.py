#!/usr/bin/env python
#coding:utf8


import os
import imp


class AutoLoad(object):

    def __init__(self, module_name):
        DIR = os.path.dirname(os.path.abspath(__file__))
        self.module_dir = os.path.join(os.path.dirname(DIR), "modules")
        self.module_name = module_name

    def isValidModule(self):
        return self._load_module()

    def _load_module(self):
        ret = False
        for filename in os.listdir(self.module_dir):
            if filename.endswith(".py"):
                #module_name = filename.split('.')[0]
                module_name = filename.rstrip(".py")
                if module_name == self.module_name:
                    fp, filename, desc = imp.find_module(module_name, [self.module_dir])
                    if not fp:
                        continue
                    try:
                        self.module = imp.load_module(module_name, fp, filename, desc)
                        ret = True
                    except Exception,e:
                        fp.close()
                    break
            else:
                print "not found"
        return ret


if __name__ == "__main__":
    at = AutoLoad('abc')
    at.isValidModule()
