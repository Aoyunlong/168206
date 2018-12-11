# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 22:07:05 2018

@author: 云龍
"""



start='hit'
end='cog'

adict =[ 'hot','dot','dog','lot','log','dit']

def find_path(start,end,paths):
    if start==end:
        return "start=end"
    else:
        visited=[]
        visited.append(start)
        for word in visited:
            temp=word
            for i in range(len(word)):
                for j in range(ord('a'),ord('z')+1):
                    word=word[:i]+chr(j)+word[i+1:]
                    print(word)
                    if word in paths and word not in visited:
                        visited.append(word)
                        #print(word)
                    if word==end:
                        visited.append(word)
                        print("the path is :")
                        print (visited)
                        return
                word=temp  #让字母回归原位

find_path(start,end,adict)

