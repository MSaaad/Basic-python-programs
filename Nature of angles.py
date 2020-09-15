#Nature of triangles
x=10
while x:
    print('Enter the three angles.... ')
    a=float(input('Enter first angle: '))
    b=float(input('Enter the second angle: '))
    c=float(input('Enter the third angle: '))
    if (a+b+c!=180):
        print('\nNot a triangle')
    elif (a==b and b==c and c==a):
        print('\nEquilateral triangle')
    elif (a==b or b==c or c==a):
        print('\nIsoseles Triangle')
    elif(a!=b and b!=c and c!=a):
        print('\nScalene Triangle')
        
    
