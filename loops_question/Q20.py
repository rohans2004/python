# 20.Print the Fibonacci series up to N terms using a for loop.
a = 0 
b = 1 
num = int(input('ENter number :'))
print(f'Fibbonachi series of {num} number will look like : ' , end = '')
for i in range (num):
    print(a , end = ' ')
    a , b = b , a + b
print()