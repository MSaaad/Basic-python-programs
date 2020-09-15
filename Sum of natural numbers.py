#python program to find sum of natural numbers
num=1
while True: #As long as the condition is true
    num=int(input('Enter the number you want for the sum:'))
    if num<0:
       print('Negative numbers are not Natural numbers')
       break
    elif num==0:
        print('0 is not a natural number')
        break
    sum=0
    count=0 #USING COUNTER VARIABLE
    while count<num:
        count=count+1 
        sum=sum+count #ADDING IN COUNTER VARIABLE
    print('The sum of first',num,'natural number is',sum)


 
