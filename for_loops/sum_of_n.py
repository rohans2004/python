#counting the sum from 1 to user input

num = int(input('Enter number :'))      #taking user input

count = 0   #initializing a counter variable 

for i in range ( 1 , num + 1 , 1):
    count  = count + i      #adding digit one by one

print(f'Sum = {count}')