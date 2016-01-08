#!/usr/bin/env python
#coding:utf8


import os


class AutoLoad(object):

    def __init__(self, module_name):
        DIR = os.path.dirname(os.path.abspath(__file__))
        self.module_dir = os.path.join(os.path.dirname(DIR), "modules")
        self.module_name = module_name

    def isValidModule(self):
        return self._load_module()

    def _load_module(self):
        ret = False
        print os.listdir(self.module_dir)





if __name__ == "__main__":
    at = AutoLoad('abc')
    at.isValidModule()
