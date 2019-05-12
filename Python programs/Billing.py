print('\t\tWELCOME!!')
print('\nB=Burger','\nS=Sandwhich','\nP=Pizza','\nF=French Fries')
order=int(input('How many types of snacks you need to order: '))
B=200;F=50;S=100;P=500
def orderB():
    orderB=B*quantity
    print(orderB) 
def orderS():
    orderS=S*quantity
    print(orderS)
def orderP():
    orderP=P*quantity
    print(orderP)
def orderF():
    orderF=F*quantity
    print(orderF)
while order==1:
    Snack=input('Enter the snack you want to order:')    
    quantity=int(input('Please provide Quantity:'))
