# Check if a given number is prime or not using a for loop.
n = int (input ('enter number :'))
is_prime = True
for i in range ( 2 , n):
    if n % i == 0:
        is_prime = False
if is_prime:
    print("The number is Prime ")
else : 
    print("The number is NOT prime ")