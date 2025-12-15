# 12. Given a list of numbers, stop printing when the number 0 is found. (Use break)
#     ○ Example: [3, 4, 1, 0, 7, 9] → stop at 0

l = [3, 4, 1, 0, 7, 9]
for i in l:
    if i == 0:
        break
    else:
        print(i , end = ' ')