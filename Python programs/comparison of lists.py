a=[]
b=[]
for x in (a,b):
    a=input('Enter first series:')
    b=input('Enter second series:')
    
    if (a==b and b==a):
        print('Common elements',)
    if (a!=b or b!=a):
        print('Uncommon elements',)
    
