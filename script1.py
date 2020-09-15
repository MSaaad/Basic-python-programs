def sum(n):
  
   if n <= 1:
       return n
   else:
       return n + sum(n-1)
a=int(input('How many times you want a Sum?'))    
for i in range(a):    
    num = int(input("Enter a number please: "))
    if num < 0:
       print("Enter a positive number")
    else:
       print('sum',sum(num))
   
