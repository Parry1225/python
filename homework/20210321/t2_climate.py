"""
Topic:輸入溫度，如果溫度>=40度C,顯示: 太熱,
　　　如果溫度<= 10 顯示:太冷, 其他：舒適:

Show:Please input temperature:"
Input1:40
Output:It's too hot.
"""
a=int(input('輸入溫度'))
if a<=10:
    print('太冷')
elif a>=40:
    print('太熱')
else:
    print('舒適')
