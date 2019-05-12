#Palindrome using while
a=10
while a:
    a=input('Enter a palindrome word: ')
    b=a[::-1]
    if a==b:
        print('This is palindrome')
    if a!=b:
        print('This is not a palindrome')
