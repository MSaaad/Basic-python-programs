def time_Calc():
    data=int(input('Enter the data in terms of Year,Weeks or Days:'))
    choice=input('''You have to input the data in the form of
Y=Years,D=Days and W=Weeks:''')
    if choice=='Y':
        sec=data*365*24*60*60
        print('In seconds =',sec,'s')
        minute=data*365*24*60
        print('In minutes =',minute,'min')
        hour=data*365*24
        print('In hours =',hour,'hr')

    if choice=='W':
        sec=data*7*24*60*60
        print('In seconds =',sec,'s')
        minute=data*7*24*60
        print('In minutes =',minute,'min')
        hour=data*7*24
        print('In hours =',hour,'hr')

    if choice=='D':
        sec=data*24*60*60
        print('In seconds =',sec,'s')
        minute=data*24*60
        print('In minutes =',minute,'min')
        hour=data*24
        print('In hours =',hour,'hr')
time_Calc()
