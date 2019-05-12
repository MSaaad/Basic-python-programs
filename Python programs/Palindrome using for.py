#Palindrome using for
for a in (0,0):
    a=input('Enter a Palindrome: ')
    b=a[::-1]
    if a==b:
        print('Palindrome')
        continue
    if a!=b:
        print('Not a Palindrome')
        break
