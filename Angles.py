#Triangles
a=float(input('Enter first angle: '))
b=float(input('Enter second angle: '))
c=float(input('Enter third angle: '))
if (a+b+c!=180):
    print('\nThis is not a Trianle')
elif(a==b and b==c and c==a): 
    print('\nEquilateral triangle')
elif(a==b or b==c or c==a):
    print('\nIsoceles Triangle')
elif(a!=b and b!=c and c!=a):
    print('\nScalene Triangle')
    
