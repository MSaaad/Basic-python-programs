a=[1,2,3,4,5,2,3]
b=set(a)
c=[]
for x in a:
    if x in b:
        b.remove(x)
    else:
        c.append(x)
