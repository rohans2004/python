# 13. Check if a given number is prime or not using a for loop.
num = int(input('Enter number :'))
count = 0 
for i in range(2 , num ,1 ):
    if num%i == 0 :
        count += 1
if count == 0 :
    print(f'The Number {num} is a Prime Number')
else :
    print(f'The Number {num} is NOT a Prime Number.')