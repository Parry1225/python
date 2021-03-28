import turtle as t
t.color('yellow')
t.shape('circle')
t.penup()
for stop in range(5,100,2):
    t.stamp()
    t.forward(stop)
    t.right(25)

    t.speed(0)