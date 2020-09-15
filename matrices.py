print('FIRST MATRIX')
a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
c=int(input('Enter third number:'))
d=int(input('Enter fourth number:'))

first_matrix=[[a,b],[c,d]]

print('SECOND MATRIX')
e=int(input('Enter fifth number:'))
f=int(input('Enter sixth number:'))
g=int(input('Enter seventh number:'))
h=int(input('Enter eighth number:'))

sec_matrix=[[e,f],[g,h]]

order1=first_matrix[0][0]+sec_matrix[0][0]
order2=first_matrix[0][1]+sec_matrix[0][1]
order3=first_matrix[1][0]+sec_matrix[1][0]
order4=first_matrix[1][1]+sec_matrix[1][1]

print('|',order1 , order2,'|')
print('|',order3 , order4,'|')
