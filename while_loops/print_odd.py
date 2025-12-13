#basic way to print Odd 
n = int(input('enter number :'))
while ( n > 0 ):
    if n%2 != 0 :
        print(n)
    n -= 1

#Simple way to print the Odd numbers 
n = int(input('enter number :'))
i = 1 
while ( i <= n ):
    if i%2 != 0 :
        print(i)
    i += 1

#advanced way to print the Odd number 
n = int(input('enter number :'))
i = 1 
print('Odd number are :',end = ' ')
while ( i <= n ):
    
    if i%2 != 0 :
        print(i,end = ' ')
    i += 1