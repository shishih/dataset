# coding: utf-8 -*-

import os
import string

def getname(path):
    nameList=[]
    initList=os.listdir(path)
    for filename in initList:
        nameList.append(os.path.splitext(filename))
    return nameList
def getSrt(nameList,file,path):
    for name in nameList:
        if name[1]=='.srt':
            file.write(name[0]+name[1]+'\n')
def getInput(nameList,file,path):
    srtName=''
    videoname=''
    txtname=''
    nameDic={}
    for name in nameList:
		if string.find(name[0],' ')!=-1:
			print 'error'
		if name[1]=='.mp4':
            if name[0]==txtname:
                file.write(path+name[0]+name[1]+',,'+srtName+'\n')
            else:

		elif name[1]=='.srt':
			srtName=path+name[0]+'.txt'
def main():
    # path='E:\users\yushiy\video\profiling'
    path='E:/users/yushiy/video/profiling/'
    nameList=getname(path)
    # print nameList
    # file=open('srtlist_sentiment.txt','a')
    # getSrt(nameList,file,path)
    # file.close()
    file=open('inputList.txt','a')
    getInput(nameList,file,path)
    file.close()

if __name__ == '__main__':
    main()