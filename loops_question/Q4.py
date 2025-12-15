# 4. Take a number from the user and print its multiplication table (1–10).
number = int(input('Enter Number : '))
for i in range ( 1 , 11 , 1 ):
    print(f'{number} * {i} = { number * i }')