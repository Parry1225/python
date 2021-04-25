'''
請使用def畫出10個，不同顏色的屋頂，及位置的房子
顏色用list用代入
'''
color=['red','blue','peru','yellow','green','brown','darkred','maroon','saddlebrown','sienna']
import turtle as t
import random
t.speed(100)
def roof(x,y,color):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.setheading(0)
    t.color(color)
    t.penup()
    t.forward(60)
    t.pendown()
    t.forward(60)
    t.right(60)
    t.forward(60)
    t.right(120)
    t.forward(120)
    t.right(120)
    t.forward(60)
    t.right(60)
    t.end_fill()
def horse(x,y,color):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.setheading(0)
    t.forward(90)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.end_fill()
for i in range(1,11):
    a=(random.randint(-150,150))
    b=(random.randint(-150,150))
    roof(a,b,color[(random.randint(1,9))])
    horse(a+45,b-53,color[(random.randint(1,9))])