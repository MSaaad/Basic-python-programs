#FINDING NUMBERS
a=10
b=23

while a:
    a=float(input('Enter the integer:'))
    if int(a)!=float(a):
        print('not a integer')
    elif a<0:
        print('negative')
    elif a>0:
        print('Positive')
    elif a==0:
        print('Zero')   
    
