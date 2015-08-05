# -*_ coding: utf-8 -*-
import os
import string

#执行重命名功能
path = 'F:/Research/Video/Dataset/pathtest'
# path ='E:/users/yushiy/video/profiling'
filelist=open('lookup_table2num.txt','a')
no=0
file2num=[]
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        # if string.find(file,' ')!=-1:
        print 'original: ',file
        filelist.write(str(file)+',')
        
        name=os.path.splitext(file)
        print name[0],'ext',name[1]
        if name[1]=='.mp4' or '.description':
            mainname=name[0]
        if name[1]=='.xml':
            mainname=name[0].replace('.annotations','')
            continue;
        if name[1]=='.srt' or '.txt':
            mainname=name[0].replace('.en','')
        if name[1]=='.json':
            mainname=name[0].replace('.info','')
            print 'true'
        print 'mainname:',mainname

        filelist.write(str(mainname)+',')
        if mainname in file2num:
            pass
        else:
            file2num.append(mainname)
        newname=str(file2num.index(mainname))+name[1]
        print 'new name:',newname
        # filelist.write(newname)

        # newname = file.replace(' ','_')
        # print newname
        # print file

        if newname in os.listdir(path):
            os.remove(path+'/'+file)
        else:
            filelist.write(str(newname)+'\n')
            os.rename(os.path.join(path,file),os.path.join(path,newname))

filelist.close()

#打印重命名后的文件名列表        
# for file in os.listdir(path):
#     if os.path.isfile(os.path.join(path,file))==True:
#         print file