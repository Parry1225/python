"""
輸入一數字n為尋找的區間範圍, 找出區間範圍
3,7的倍數顯示在螢幕上，其餘不顯示，可使用取餘數函式%


e.g.
input:20
output:
3
6
7
9
12
14
15
18
"""
n=int(input('你想要的數字?'))
b=3
x=7
for i in  range(1,n):
    if (i!=b)&(i!=x):
        continue
    elif i==b:
        print(b)
        b+=3
    elif i==x:
        print(x)
        x+=7
    #elif i!=x:
        #continue
