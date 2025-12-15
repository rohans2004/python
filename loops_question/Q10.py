# 10. Print all characters of a string except spaces. (Use continue)
str = input('Enter string : ')
for i in str :
    if i == ' ':
        continue
    else:
        print(i , end = '')