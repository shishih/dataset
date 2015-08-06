# -*_ coding: utf-8 -*-
import os
import string
import re

#执行重命名功能
path = 'F:/Research/Video/Dataset/pathtest'
# path = 'E:/users/yushiy/video/profiling - Copy/'

dirlist=os.listdir(path)
# print dirlist
patternAnno=re.compile(r'\.annotations$')
patternInfo=re.compile(r'\.info$')
patternEn=re.compile(r'\.en$')
namelist=[]

fp=open('namelist.txt','a')
for file in dirlist:
    mainname=patternEn.sub('',patternInfo.sub('',patternAnno.sub('',os.path.splitext(file)[0])))
    if not mainname in namelist:
        namelist.append(mainname)
    

    ext=os.path.splitext(file)[1]

    newname=str(namelist.index(mainname))+ext
    fp.write(str(namelist.index(mainname))+'$'+str(file)+'$'+newname+'\n')
    if newname in os.listdir(path):
            os.remove(path+'/'+file)
    else:
        # filelist.write(str(newname)+'\n')
        os.rename(os.path.join(path,file),os.path.join(path,newname))