import random
def roll_dice(n):
    dice=[]
    for i in range(n):
        dice.append(random.randint(1,6))
    return dice

def who_win(m,u):
    if m>u:
        print('你贏了')
    elif m<u:
        print('你輸了')
    else:
        print('平手')


num=int(input('輸入擲骰子的次數'))
user=roll_dice(num)
my=roll_dice(num)
m=sum(my)
u=sum(user)
print('my=',m)
print('user=',u)
who_win(m,u)
