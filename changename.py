# -*_ coding: utf-8 -*-
import os

#执行重命名功能
# path = 'F:/Research/Video/Dataset/pathtest'
path ='E:\users\yushiy\video\profiling'
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        newname = file.replace(' ','$')
        os.rename(os.path.join(path,file),os.path.join(path,newname))

#打印重命名后的文件名列表        
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        print file