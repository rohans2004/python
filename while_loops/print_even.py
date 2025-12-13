#basic way to print even 
n = int(input('enter number :'))
while ( n > 0 ):
    if n%2 == 0 :
        print(n)
    n -= 1

#Simple way to print the even numbers 
n = int(input('enter number :'))
i = 1 
while ( i <= n ):
    if i%2 == 0 :
        print(i)
    i += 1

#advanced way to print the even number 
n = int(input('enter number :'))
i = 1 
print('even number are :',end = ' ')
while ( i <= n ):
    
    if i%2 == 0 :
        print(i,end = ' ')
    i += 1