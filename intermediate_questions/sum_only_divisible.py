# Print the sum of all numbers from 1–100 but skip numbers divisible by 3.
sum = 0
for i in range ( 1 ,101):
    if i % 3 == 0:
        continue
    sum += i 
print(f'Sum : {sum}')