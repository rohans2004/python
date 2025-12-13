# 10. Print all characters of a string except spaces. (Use continue)
str = input("enter string :")
for i in str :
    if i == ' ':
        continue
    print(i, end = '')