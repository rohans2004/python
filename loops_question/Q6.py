# 6. Print only the vowels from a string given by the user.
vowels = 'AEIOUaeiou'
str = input('Enter string :')
for i in str:
    if i == ' ':
        print(' ', end = '')
    else:
        if i in vowels:
            print(i , end = '')
    