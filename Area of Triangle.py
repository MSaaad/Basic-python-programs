#s=a+b+c
#area=(s(s-a)*(s-b)*(s-c))**0.5
a=1;b=1;c=1
while True:
    a=float(input('Enter the first side: '))
    b=float(input('Enter the second side: '))
    c=float(input('Enter the third side: '))
    s=a+b+c
    print('The sum of sides of triangle is',s)
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print('The Area of triangle is',area)
