# D 
# C D 
# B C D 
# A B C D 

n = int (input('Enter number : '))
for i in range(n):
    for j in range(n - i - 1 , n):
        print(chr(65 + j ), end = ' ')
    print()

