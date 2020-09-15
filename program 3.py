b=list(input('Enter the list:'))
c=list(input('Enter second list:'))
for a in set(b):
    if set(b)==set(c):
        print('duplicate')
    elif set(b)!=set(c):
        print('No duplicate')

