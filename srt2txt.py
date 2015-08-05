# -*- coding: utf-8 -*-

import re
import os

def trans(fileSrt,fileTxt):
    pattern=re.compile(r'^\d{1}.+\s')
    patternRow=re.compile(r'^\d\s')
    data=fileSrt.readlines()
    for line in data:
        match=pattern.search(line)
        if match:
            pass
        else:
            matchRow=patternRow.search(line)
            if matchRow:
                pass
            else:
                fileTxt.write(line)

def main():
    # path='../video\profiling'+'\\'
    path='F:/Research/Video/Dataset/pathtest/'
    nameList=[]
    # initList=os.listdir(path)

    # fileList=open('srtlist.txt')
    # data=fileList.readlines()
    filelist=os.listdir(path)
    for line in filelist:
        name=os.path.splitext(line)
        line=path+line.strip()
        if name[1]=='.srt':            
            srtFile=line
            txtFile=line[:-3]+'txt'

            if txtFile in filelist:
                pass
            else:
                fileSrt=open(srtFile)
                fileTxt=open(txtFile,'a')
                trans(fileSrt,fileTxt)
                fileSrt.close()
                fileTxt.close()

if __name__ == '__main__':
    main()