# coding: utf-8 -*-

import os

def getname(path):
    name=[]
    nameList=os.listdir(path)
    for filename in nameList:
        name.append(os.path.splitext(filename))
def main():
    # path='E:\users\yushiy\video\profiling'
    path='F:\Research\Video\Dataset\coursera\popularity-001'
    getname(path)