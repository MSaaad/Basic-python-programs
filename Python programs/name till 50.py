name=input('Enter your name:') #Saad
length=len(name)   #4
print('Length =',length)
if length%2==0:  #Even Number
    num=51
    for i in range(length,num):    #Length of name=========num-1
        if i%2==0:
            print('even',i)
else:
    print('Your name is not an even number')
