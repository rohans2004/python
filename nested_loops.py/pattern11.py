#           A B C D E 
#         A B C D E 
#       A B C D E 
#     A B C D E 
#   A B C D E 

n = int(input('Enter Number :'))

for row in range(n,0,-1):
    for space in range(row):
        print(' ',end = ' ')
    for star in range (n):
        print(chr(65+star),end = ' ')
    print()

