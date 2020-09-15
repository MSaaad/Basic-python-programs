#MAKE A PROGRAM AND SHOW THAT WHICH ANGLE IS ACUTE,OBTUSE AND REFLEX.

A='Acute'
B='Obtuse'
C='Reflex'
A=int(input('Give angle 1: '))
B=int(input('Give angle 2: '))
C=int(input('Give angle 3: '))
if A>45:
    print('your triangle is acute')
else:
    print('not acute')
if B>90:
    print('your triangle is obtuse')
else:    
     print('not obtuse')
if C>180:
    print('your triangle is reflex')
else:
    print('not reflex')
   
