#"""
#Topic:輸入三角形三邊，判斷是否能構成三角形，
    #是三角形則顯示面積和周長，不行則顯示，無法構成三角形:

#Triangle Area formula:
#p = 1/2 (a+b+c)
#area = (p * (p - a) * (p - b) * (p - c)) ** 0.5

#e.g.
#Show:a ="
#Input1:3

#Show:b ="
#Input2:4

#Show:c ="
#Input3:5

#output:
#perimeter: 12.000000
#Area: 6.000000
#"""
a=int(input('請輸入三角形的第1邊'))
b=int(input('請輸入三角形的第2邊'))
c=int(input('請輸入三角形的第3邊'))
p = 1/2*(a+b+c)
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
if (a+b>c)and(a+c>b)and(b+c>a):
    print('周長是',(a+b+c),'面積是',(area))
else:
    print('無法構成三角形')