input_string = input("Enter string : ")
print("-----before case conversion:-----")
print(input_string)
i = 0
result = ""
while i < len(input_string):
    if input_string[i].islower():
        result = result + input_string[i].upper()
    else:
        result = result + input_string[i].lower()
    i += 1
print("-----after case conversion:-----")
print(result)
