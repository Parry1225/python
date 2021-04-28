'''
使用者輸入兩個數num1 and num2，
並使用function def 求最小公倍數
value = lcm(num1, num2)
'''
a=int(input('你的第一個數字是？'))
b=int(input('你的第二個數字是？'))
def lcm(x, y):

   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


print( a,"和", b,"的最小公倍數是", lcm(a, b))










