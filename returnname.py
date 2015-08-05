# -*_ coding: utf-8 -*-
import os
import string

#执行重命名功能
path = 'F:/Research/Video/Dataset/pathtest'
# path ='E:/users/yushiy/video/profiling'
fp=open('lookup_table2num.txt')
filelist=fp.readlines()
filelist.reverse()
no=0
file2num=[]
for file in filelist:
    file=file.strip()
    name=file.split(',')
    if os.path.isfile(os.path.join(path,name[2]))==True:

    # if newname in os.listdir(path):
    #     os.remove(path+'/'+file)
    # else:
    #     filelist.write(str(newname)+'\n')
        os.rename(os.path.join(path,name[2]),os.path.join(path,name[0]))
        print name[2],name[0]

fp.close()

#打印重命名后的文件名列表        
# for file in os.listdir(path):
#     if os.path.isfile(os.path.join(path,file))==True:
#         print file