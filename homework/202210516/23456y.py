sts=[1,10,10,1000,0,0]
def wrint(sts):
    path ='output.txt'
    f=open(path,'w')
    for i in sts:
        f.write(str(i)+"\n")
    f.close()
def line():
    path ='output.txt'
    f=open(path,'r')
    text=[]
    for line in f:
        text.append(int(line))
    print(text)
    f.close()
    return text
wrint(sts)
text=line()