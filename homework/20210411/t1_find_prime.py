"""
輸入一數字n為尋找的區間範圍, 找出區間範圍
的質數顯示在螢幕上，其餘不顯示。
"""
n=int(input('你想要的數字?'))
k = 0;
for i in  range(2,n+1):
    for j in range(1,i+1):
       a = i % j;
       if a == 0:
          k = k + 1;
    if k == 2:
       print (i)
    k=0




"""
a=i % j
print(a)
"""
