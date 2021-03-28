"""
Topic:請使用turtle及loop印出下列圖形

e.g.
turtle_stamp.jpg
可利用turtle.home()會回到原點(0.0)的特性
"""
import turtle as t
i=0
a=0
t.penup()
while i<8:
    t.home()
    t.right(a)
    t.forward(150)
    t.stamp()
    t.speed(5)
    i+=1
    a+=45
t.home()
t.stamp()