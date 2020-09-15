a=input('Enter the temperature you want in: ')
if a=='celsius':
    c=int(input('Enter a temperature in Celsius:'))
    f=9/5*c+32
    print(f)
if a=='fahrenheit':
    f=int(input('Enter the temperature in fahrenheit:'))
    c=(f-32)*5/9
    print(c)
    

