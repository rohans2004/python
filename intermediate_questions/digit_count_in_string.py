# Takeing  a number input and counting how many digits it has.
str = int(input('enter string :')) # 123
count = 0
if str.isnumeric():
    for i in str :
        if i.isdigit():
            count +=1 
    print(f'there are {count} digit in the string.')
else:
    print("enter again ...")