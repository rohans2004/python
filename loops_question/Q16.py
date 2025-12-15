# 16. Count how many vowels are in the string: "Hello Python Programmer"
str = "Hello Python Programmer"
vowel = "AEIUOaeiuo"
count = 0
for i in str :
    if i in vowel:
        count +=1
print(f"count :{count}")