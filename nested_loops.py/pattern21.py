n = int(input('Ente number : '))
# # # # # 
#       # 
#       # 
#       # 
# # # # # 

for i in range(1,n+1):
    for j in range(1,n+1):
        if j == n or i == n  or i==1 or j==1:
            print("#",end = ' ')
        else:
            print(" ",end =' ')
    print()


# 1 2 3 4 5 
# 1       5 
# 1       5 
# 1       5 
# 1 2 3 4 5 

for i in range(1,n+1):
    for j in range(1,n+1):
        if j == n or i == n  or i==1 or j==1:
            print(j,end = ' ')
        else:
            print(" ",end =' ')
    print()

# A B C D E 
# A       E 
# A       E 
# A       E 
# A B C D E 

for i in range(1,n+1):
    for j in range(1,n+1):
        if j == n or i == n  or i==1 or j==1:
            print(chr(64+j),end = ' ')
        else:
            print(" ",end =' ')
    print()