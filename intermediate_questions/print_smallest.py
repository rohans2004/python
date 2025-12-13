# Print the smallest number in a list.

str  = list(input('enter list :'))
small = str[0]
for i in str :
    if i < small:
        small = i
print(f'smallest :{small}')