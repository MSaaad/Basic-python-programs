print('GUESS THE NUMBER GAME!')
user=1
num=8
while user:
    user=int(input('Enter the number:'))
    if user<num:
        print('Your guess is too low! :(')
    elif user>num:
        print('Your guess is too High! :(')
    if user==6:
        print('But You are very close! :)')
    if user==10:
        print('But You are very close! :)')
    if user==num:
        print('You have guessed the right answer!! ;)')
        
