# 7. Given a string, print the first 5 characters only and stop. (Use break)
str = input('enter string : ')
count = 5 
for i in str:
    if count > 0 :
        print(i , end = '')
        count -= 1
