# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 23:04:08 2018

@author: 云龍
"""
#s代表小偷则题目可转化为
#A：我没有偷钻石。 s!= 1
#B：D就是罪犯。  s= 4      
#C：B是盗窃这块钻石的罪犯。  s= 2
#D：B有意诬陷我。 s!= 4

number=1 #说真话人数
for s in range(4):
    s += 1
    if number == ((s != 1) + (s == 4) + (s == 2) + (s != 4)):
        str = chr(96 + s) + "是小偷！"
        print(str)
#通用性和数学方法还在构思中