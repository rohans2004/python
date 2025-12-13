# Take 10 numbers from the user and print the highest number.
highest = None
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    if highest is None or num > highest:
        highest = num
print(f'Highest number among these 10 is {highest}')