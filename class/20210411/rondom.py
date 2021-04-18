import random as r
b=0
a=0
while a!=7:
    a=r.randint(1,10)
    print(a)
    b+=1
    if a==5:
        break

if a==7:
    print('恭喜中獎')
    print('你骰了',(b),'次')
else:
    print('game over')
    print('你骰了',(b),'次')