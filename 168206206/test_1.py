# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 15:12:03 2018

@author: 云龍
"""
'''
A：我没有偷钻石。thief != 1         [1,0,0,0]
B：D就是罪犯。thief  = 4            [000-1]
C：B是盗窃这块钻石的罪犯。thief=2    [0-100]
D：B有意诬陷我。thief != 4          [0001]
for s in range(4):
    s += 1
    if number == ((s != 1) + (s == 4) + (s == 2) + (s != 4)):
        str = chr(96 + s) + "是小偷！"
        print(str)
'''

#上述算法改进可以根据输入不同而得结果
number=1 #说真话人数
#将所说话转换为数组表示1表示不是小偷，-1表是小偷，
abcd=[[1,0,0,0],[0,0,0,-1],[0,-1,0,0],[0,0,0,1]]

#假设小偷为s
a=0 #当假设小偷为s时说真话个数
for s in range(4):
    s+=1
    for i in abcd:
        #print(i)
        for j in range(len(i)):
            #print(i[0])
            if i[j]==1:
                if s!=j+1:
                    a=a+1
                    #print('dhcfv+',s,j,a)
            if i[j]==-1:
                if s==j+1:
                    a+=1
                    #print(s,j,a)
    print("假设小偷是"+ chr(64 + s)+"则说真话的人数是%d" %a )
    
    if number==a:
        str = chr(96 + s) + "是小偷！"
        print(str)
    a=0
'''
输出结果：
      
假设小偷是A则说真话的人数是1
a是小偷！
假设小偷是B则说真话的人数是3
假设小偷是C则说真话的人数是2
假设小偷是D则说真话的人数是2
'''   
        
