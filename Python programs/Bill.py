a='Enter first snack you want to order:'
b='Enter second snack you want to order:'
c='Enter third snack you want to order:'
d='Enter fourth snack you want to order:'
print('\t\tWELCOME!')
print('Please select from the following menu:')
print('\nBurger','\nFrench Fries','\nPizza','\nSandwhiches')
B=200 #BURGER 
F=50 #FRENCH FRIES
P=500 #PIZZA
S=100 #SANDWHICHES
x=1
for order in (B,F,P,S):
    x=int(input('How many types of snacks you want to order:'))
    if x==1:
        input(a)
        x1=int(input('Please provide quantity:'))
        print('You have ordered!')
        y=order*x1
        print(y)
        
    elif x==2:
        input(a)
        x1=int(input('Please provide quantity:'))
        y=order*x1
        input(b)      
        x2=int(input('Please provide quantity:'))
        y1=order*x2
        print('You have ordered!')
        print(y+y1)      
        

