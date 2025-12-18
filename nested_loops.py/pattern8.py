
# 1 2 3 4 5 
#   1 2 3 4 
#     1 2 3 
#       1 2 
#         1 
n = int(input('Enter number : '))
for i in range(n , 0 , -1 ):
    #printing spaces
    for space in range(n - i):
        print(" " ,end = ' ')
    #printing numbbers
    for num in range(1 , i + 1 ):
        print(chr(64 + num) , end = ' ')
    print() 


# A B C D E 
#   A B C D 
#     A B C 
#       A B 
#         A 
n = int(input('Enter number : '))
for i in range(n , 0 , -1 ):
    #printing spaces
    for space in range(n - i):
        print(" " ,end = ' ')
    #printing numbbers
    for num in range(1 , i + 1 ):
        print(chr(64 + num) , end = ' ')
    print()    