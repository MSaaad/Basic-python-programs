x=int(input('Enter Any number: '))
for i in range(1,x+1):
    c=str(i)
    if 10<i<14:
        print(c,'th',sep='')
    elif c[-1]=='1':
        print(c,'st',sep='')
    elif c[-1]=='2':
        print(c,'nd',sep='')
    elif c[-1]=='3':
        print(c,'rd',sep='')
    else:
        print(c,'th',sep='')
