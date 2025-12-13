#finding factorial with while loop 
num = int(input('Enter Number :'))
fact = 1                            #initialiazing an variable name fib from 1 
while( num > 0 ):
    fact = fact * num
    num -= 1
print(f'Factorial of the number is {fact}')