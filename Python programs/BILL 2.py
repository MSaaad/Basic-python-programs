print('\t\tWELCOME!!')
print('\nB=BURGER','\nP=PIZZA','\nS=SANDWHICH','\nF=FRENCH FRIES')
e=0
sequence=['first','second','third','fourth']
order=[]
k=[]
m=[]

a=int(input('How many types of snack you need to order: '))
for x in range(0,a):
    b=input('Enter the order you want '+str(sequence[e])+':' )
    e=e+1
    qua=int(input('Enter the Quantity:'))
    k.append(qua)
    if b=='B':
        b=200*qua
        m.append('Burger(s)')
        order.append(b)
    elif b=='F':
        f=50*qua
        m.append('French fries')
        order.append(f)
    elif b=='P':
        p=500*qua
        m.append('Pizza(s)')
        order.append(p)
    elif b=='S':
        s=100*qua
        m.append('Sandwhich(es)')
        order.append(s)
    else:
        print('No given option selected')
        break
    
p=0;q=0;r=0;t=1;v=0
for n in range(0,a):
    print(str(k[p])+ ' ' +m[q]+ ' RS ' +str(order[r])+ ' PKR')
    t=order[r];v=v+t;p=p+1;q=q+1;r=r+1
    print('TOTAL= '+str(v)+' RS')
    print('THANK YOU FOR THE ORDER.....')
    print('HAVE A NICE DAY!!!')





