a=1;b=1;c=1
while True:
    a=int(input('Enter first number:'))
    b=int(input('Enter second number:'))
    c=int(input('Enter third number:'))
    d=b**2-(4*a*c)
    x=2*a
    X1=(-b+(d)**0.5)/x
    X2=(-b-(d)**0.5)/x
    print('First equation is',X1)
    print('Second equation is',X2)
