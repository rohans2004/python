# Counting the number of vowels in a given string using a loop.
str = input("enter string :")
count = 0 
vowel = 'AEIOUaeiou'
for i in str :
    if i in vowel:
        count += 1
print(f'there are {count} vowel in the string .')