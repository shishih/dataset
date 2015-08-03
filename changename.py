# -*_ coding: utf-8 -*-
import os

#执行重命名功能
path = 'F:/Research/Video/Dataset/pathtest'
# path ='E:\users\yushiy\video\profiling'
filelist=open('lookup_table.txt','a')
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        filelist.write(str(file)+',')
        newname = file.replace(' ','_')
        newname = file.replace('$','_')
        filelist.write(str(newname)+'\n')
        os.rename(os.path.join(path,file),os.path.join(path,newname))
filelist.close()

#打印重命名后的文件名列表        
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        print file