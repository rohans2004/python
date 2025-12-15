# 14. Print the factorial of a number using a for loop.
#     ○ Example: 5 → 120

num = int(input("Enter number : "))
fact = 1 
for i in range(1 , num + 1 ):
    fact *= i
print(f"Factorial of {num} is {fact}")
