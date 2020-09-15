print("\tPALINDROME")
a=10
while a:
    a=input('Enter a palindrome word: ')
    b=a[::-1]
    if len(a)==1:
        print('Single letter not a palindrome')
    if len(a)!=1 and a==b:
        print('Palindrome')
    elif a!=b:
        print('Not a palindrome')
        
