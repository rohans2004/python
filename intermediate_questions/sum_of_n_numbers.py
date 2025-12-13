# Printing the sum of first n natural numbers.
num = int(input('Enter number :'))
sum = 0 
for i in range (1,num+1):
    sum += i 
print(f'Sum = {sum}')