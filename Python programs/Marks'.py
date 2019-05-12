marks=1
while True:
    marks=int(input('Enter the Marks:')) 
    if marks>=88:
        print('Your grade is A and Grade point is 4.0')
    elif marks>=80:
        print('Your grade is A- and Grade point is 3.7')
    elif marks>=75:
        print('Your grade is B+ and Grade point is 3.4')
    elif marks>=70:
        print('Your grade is B and Grade point is 3.0')
    elif marks>=67:
        print('Your grade is B- and Grade point is 2.7')
    elif marks>=64:
        print('Your grade is C+ and Grade point is 2.4')
    elif marks>=60:
        print('Your grade is C and Grade point is 2.0')
    elif marks>=57:
        print('Your grade is C- and Grade point is 1.7')
    elif marks>=54:
        print('Your grade is D+ and Grade point is 1.4')
    else:
        if marks<54:
            print('Your grade is D and your grade point is 1.0')
