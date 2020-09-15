#Recursive function
def fact_rec(n):
    if n<0:
        return -1
    elif n<2:
        return 1
    else:
        return n*fact_rec(n-1)
def fib_rec(n):       # 0 1 1 2 3 5 8 13 21
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib_rec(n-2)+fib_rec(n-1)

x=int(input('Enter:'))
for i in range(0,x+1):
    print(fib_rec(i))
