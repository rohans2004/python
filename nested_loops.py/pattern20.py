# 1 2 3 4 5 6 7 8 9 
#   1 2 3 4 5 6 7 
#     1 2 3 4 5 
#       1 2 3 
#         1 
#       1 2 3 
#     1 2 3 4 5 
#   1 2 3 4 5 6 7 
# 1 2 3 4 5 6 7 8 9 

n = int (input('Enter number : '))

for i in range(n-1):
    # spaces
    for space in range(i):
        print(" ", end=" ")

    # stars
    for star in range(1,2*(n - i)):
        print(star, end=" ")
    print()
for i in range(1,n+1):
    for space in range (n - i):
        print(" " , end = ' ')
    for star in range(1,2*i  ):
        print(star, end = ' ')
    print()
print()
# A B C D E F G H I 
#   A B C D E F G 
#     A B C D E 
#       A B C 
#         A 
#       A B C 
#     A B C D E 
#   A B C D E F G 
# A B C D E F G H I 

for i in range(n-1):
    # spaces
    for space in range(i):
        print(" ", end=" ")

    # stars
    for star in range(1,2*(n - i)):
        print(chr(64+star), end=" ")
    print()
for i in range(1,n+1):
    for space in range (n - i):
        print(" " , end = ' ')
    for star in range(1,2*i  ):
        print(chr(64+star), end = ' ')
    print()