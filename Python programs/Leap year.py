print('\tLEAP YEAR!')
year='string'
while True:
    year=int(input('Enter the year: '))
    if len(str(year))!=4:
        print('Please enter a four digit input!')
        break
    if year%4==0:
        print('This is a leap year')
    elif year%400==0:
        print('This is a Leap year')
    elif year%100==0:
        print('This is a Leap year')
    else:
        print('Not a leap year')
