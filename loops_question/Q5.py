# 5. Count how many numbers between 1 to 100 are divisible by 7.
count = 0 
for i in range ( 1 , 101 , 1 ):
    if i%7 == 0 :
        count += 1
print(f'There are {count} numbers which are divisible by 7.')





