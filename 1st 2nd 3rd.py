#num=0
y=0
x=int(input('Enter the number of terms: '))
for i in range(0,x+1):
    y=y+1
    if y%100==11 or y%100==12 or y%100==13:
        print(y,'th',sep='')
    elif y==1 or (y%10==1):
        print(y,'st',sep='')
    elif y==2 or (y%10==2):
        print(y,'nd',sep='')
    elif y==3 or (y%10==3):
        print(y,'rd',sep='')
    elif y%10!=1:
        print(y,'th',sep='')
  
  
