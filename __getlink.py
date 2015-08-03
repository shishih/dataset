# coding: utf-8 -*-

import os

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
    for name in nameList:
        if name[1]=='.mp4':
            file.write(path+name[0]+name[1]+',,'+srtName+'\n')
        elif name[1]=='.srt':
            srtName=path+name[0]+'txt'
def main():
    # path='E:\users\yushiy\video\profiling'
    # path='E:/users/yushiy/video/profiling/'
    path='F://Research/Video/Dataset/pathtest'
    nameList=getname(path)
    print nameList
    file=open('srtlist.txt','a')
    getSrt(nameList,file,path)
    file.close()
    file=open('inputList.txt','a')
    getInput(nameList,file,path)
    file.close()

if __name__ == '__main__':
    main()