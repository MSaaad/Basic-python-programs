def fact():
    x=int(input('Enter a number:'))
    factorial=1
    for i in range(1,x+1):
        factorial=factorial*i
        yield factorial
   
