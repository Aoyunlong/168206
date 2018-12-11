# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 22:27:05 2018

@author: 云龍
"""

start='hit'
end='cog'

adict =[ 'hot','dot','dog','lot','log']
def isOneDiff(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False

def findLadders(start, end, dt):
    ret = []
    def loop(wa, wb, lt,res=[]):
        for i in lt:
            if isOneDiff(wa, i) and isOneDiff(i, wb): 
                r= res.copy()
                r.append(wa)
                r.append(i)
                r.append(wb)
                ret.append([r,len(r)])
            if isOneDiff(wa, i) and not isOneDiff(i, wb):
                r = res.copy()
                r.append(wa)
                lt_copy = lt.copy()
                try:
                    lt_copy.remove(wa)  
                except:
                    pass
                loop(i, wb, lt_copy, r)
    loop(start, end, dt)
    print(ret)
    return ret

ret=findLadders(start, end, adict)
ret_y=[y for[x,y] in ret]#把所有路径长度组成新列表
word=min(ret_y)#计算最短路径长度
print('最短路径为：')
for ret_A in ret:
    for i in range(len(ret_A)):
        if (ret_A[i]==word):
             print(ret_A)#输出最短路径
