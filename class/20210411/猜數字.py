import random as r
a=r.randint(1,100)
b=0
c=1
d=100
print(a)
while b!=a:
    b=int(input('你要猜的數字'))
    if b>a:
        if d>b:
            d=b
    elif b<a:
        if c<b:
            c=b

    print(c,'到',d)
print('恭喜猜中')