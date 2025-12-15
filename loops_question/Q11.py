# 11. Print the sum of all numbers from 1–100 but skip numbers divisible by 3.
sum = 0 
for i in range( 1 ,101 , 1 ):
    if i%3 == 0 :
        continue
    else:
        sum += i
print(f'Sum of all numbers from 1–100 but skip numbers divisible by 3 is {sum}')