"""
Topic:請使用turtle及loop及time.sleep(1)印出秒針動畫

e.g.
import time
time.sleep(1)
"""
i=6
import turtle as t
t.speed(-100)
import time
while True:
    t.clear()
    t.penup()
    t.home()
    t.right(90)
    t.forward(250)
    t.left(90)
    t.pendown()
    t.circle(250)
    #t.clear()
    t.penup()
    t.home()
    t.left(90)
    t.right(i)
    t.pendown()
    t.forward(250)
    time.sleep(1)
    i+=6
