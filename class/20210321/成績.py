g=int(input('你的成績是多少?'))
if g>90:
    print('你的等第:UR')
elif g>80 and g<90:
    print('你的等第:SSR')
elif g>70 and g<80:
    print('你的等第:SR')
elif g>60 and g<70:
    print('你的等第:R')
elif g<60:
    print('你的等第:U')