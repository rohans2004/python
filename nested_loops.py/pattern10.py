#           1 2 3 4 5 
#         1 2 3 4 5 
#       1 2 3 4 5 
#     1 2 3 4 5 
#   1 2 3 4 5 

n = int(input('Enter Number:'))
for row in range(n,0,-1):
    for space in range(row):
        print(" ",end = ' ')
    for star in range(1,n+1):
        print(f"{star}",end = ' ')
    print()