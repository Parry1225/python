from microbit import *
import time as t
l=['boat0','boat1','boat2']
s=0.001
boat0 = Image("00600:"
              "06960:"
              "69996:"
              "06960:"
              "00600")
boat1 = Image("00900:"
              "09690:"
              "96669:"
              "09690:"
              "00900")
boat2 = Image("00300:"
              "03530:"
              "35553:"
              "03530:"
              "00300")
while True:
    for i in l:
        display.show(i)
        t.sleep(s)






