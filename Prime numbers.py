x=1
prime=50
while x<prime:
    x=int(input('Enter any number:'))
    print('Prime numbers between 2 and',x,'are')
    for z in range(2,x):
        for y in range(2,z):
            if z%y==0:
                break
        else:
            print(z)
            
    
