"""
1. 初始血量:10點
2. 初始錢:0元
3. 冒險者攻擊力:1-3點
4. 怪物攻擊力:1點
1. 獲得紅藥水:1-3點血量
1. 獲得錢袋:10-30元
1. 擊敗怪物可以獲得10-20元
2. 回合制，冒險者有先攻擊的優先權
3. 冒險者隨機對怪物產生1-3點傷害
4. 怪物生命隨機2-10點，攻擊力1點
5. 戰鬥結束後，更新冒險者狀態
status[0] = 1活著，0死亡
 status[1] = 剩餘生命
 status[2] = 剩餘金幣
 尋問用魔法/普通攻擊
增加魔法攻擊(4-8點攻擊力)，每次需使用1點魔力
技能可以消耗魔力額外計算
新增商店(2(回魔)/1(回血)/q(離開)/3(技能))
  回魔藥水，一瓶100元/5-8點魔力，錢不夠無法購買
  回血藥水，一瓶100元/3-6點體力，錢不夠無法購買
  技能，第一個100元，第二個150，第3個200元，錢不夠無法購買
"""
import random as r
import time as t

def event1(hp):
    hpp = r.randint(1,3)
    hp+=hpp
    print('你回復了%d生命,你現在的生命是%d'%(hpp,hp))
    return hp
def event2(money):
    moneyy=r.randint(10,30)
    money=money+moneyy
    print('你撿到了%d塊錢,你現在有%d塊錢'%(moneyy,money))
    return money
def event3(hp,money,magic,skill):
    bedman_hp=r.randint(2,10)
    while True:
        art=r.randint(100,101)
        maggc=int(input('請問你是否要選擇魔攻1.是2.否'))
        if maggc==1:
            if magic>=3:
                if skill==0:
                    mag=r.randint(4,8)
                    print('你打了壞人%d滴血'%(mag))
                    bedman_hp-=mag
                    print('壞人剩下%d滴血'%(bedman_hp))
                    t.sleep(1)
                    magic-=1
                if skill==1:
                    mag=r.randint(1,2)
                    print('你打了壞人%d滴血'%(mag))
                    bedman_hp-=mag
                    print('壞人剩下%d滴血'%(bedman_hp))
                    t.sleep(0.5)
                    mag=r.randint(1,2)
                    print('你打了壞人%d滴血'%(mag))
                    bedman_hp-=mag
                    print('壞人剩下%d滴血'%(bedman_hp))
                    t.sleep(0.5)
                    mag=r.randint(1,2)
                    print('你打了壞人%d滴血'%(mag))
                    bedman_hp-=mag
                    print('壞人剩下%d滴血'%(bedman_hp))
                    t.sleep(0.5)
                    magic-=2



        elif maggc==2:
            print('你打了壞人%d滴血'%(art))
            bedman_hp-=art
            print('壞人剩下%d滴血'%(bedman_hp))
            t.sleep(1)


        if bedman_hp>0:
            hp-=1
            print('你剩下%d滴血'%(hp))
            t.sleep(1)
        elif bedman_hp<1:
            print('you kill bedman')
            monery=r.randint(10,20)
            money+=monery
            print('你得到了%d元，你現在有%d元'%(monery,money))
            break
    return hp,money,magic,skill
def store(money,hp,magic,skill):
    if money>=100:
        m=input('請選擇你要購買的物品1.生命藥水2.魔法藥水3.魔法技能4.q離開')
        if m=='q':
            print('你來到了商店')
        else:
            print(m)
            if m=='1':
                print('你花100塊購買生命藥水')
                hp+=r.randint(3,6)
                print('你回復的生命')
                money-=100

            elif m=='2':
                print('你花100塊購買魔法藥水')
                magic+=r.randint(5,8)
                money-=100

            elif m=='3':
                mo=input('請輸入你想要購買的技能(只要在購買下一次前一個技能就會被刷新)1.流星雨2.龍捲風3.分身斬')
                if mo=='1':
                    skill=1
                    money-=100


                if mo=='2':
                    if money>=150:
                        money-=150
                        skill=2
                if mo=='3':
                    if money>=200:
                        money-=200
                        skill=3



    return money,hp,magic,skill

question=str(input('輸入go即可開始遊戲'))
if question=='go':
    HP=10
    money=0
    magic=2
    skill=0
    while True:
        game=r.randint(1,4)
        if game==1:
            HP=event1(HP)
            game=r.randint(1,4)

        if game==2:
            money = event2(money)
            game=r.randint(1,4)

        if game==3:
            HP,money,magic,skill=event3(HP,money,magic,skill)
            game=r.randint(1,4)

        if game==4:
            money,HP,magic,skill=store(money,HP,magic,skill)
            game=r.randint(1,4)

        if HP<1:
            print('you died')
            break