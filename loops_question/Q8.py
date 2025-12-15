# 8. From numbers 1 to 20, skip odd numbers and print only squares of even numbers.
for i in range(1 ,21 ,1):
    if i%2 != 0 :
        continue
    else:
        print(f'Square of {i} is {i*i}')