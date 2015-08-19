# coding: utf-8 -*-

import os 
import json

class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


path='E:/users/yushiy/video/sentiment/'
initList=os.listdir(path)
for filename in initList:
    name=os.path.splitext(filename)
    if name[1]=='.json':
        with open(filename, 'r') as f:
            data = json.load(f,object_hook=JSONObject)
