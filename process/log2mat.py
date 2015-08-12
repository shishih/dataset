# -*_ coding: utf-8 -*-


import re

file=open('790.log')
data=file.readlines()
file.close()

pattern=re.compile(r' \d+?\s')

file=open('790.txt','a')

for i in range((len(data))):
    if i > 9 and i < len(data)-4:
        match=pattern.findall(data[i]);
        for number in match:
            print number[1:].strip()
            file.write(number[1:].strip()+'\n')

file.close()
