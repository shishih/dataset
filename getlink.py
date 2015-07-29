# -*- coding: utf-8 -*-

import re

videolink=link+‘videos’
data=html.read()

pattern=re.compile(r'/watch?v=.{11}')

match=pattern.match(data)
for video in match.group():
    file.write(str(video)+'\n')