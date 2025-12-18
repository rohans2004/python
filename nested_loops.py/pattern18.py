# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 

n = int (input('Enter number :'))
for i in range(5 , 0 , -1 ):
    for j in range(1,i+1):
        print(j,end = ' ')
    print()

# 1 
# 1 2 
# 1   3 
# 1     4 
# 1 2 3 4 5

n= int (input('Enter Number :'))
for i in range(1,n+1):
    for j in range(1,i+1):
        if i==n or i == j or j == 1 :
            print(j,end = ' ')
        else:
            print(" ",end = ' ')
    print()


# 1 2 3 4 5 
# 2     5 
# 3   5 
# 4 5 
# 5 

n = int (input('Enter Number : '))

for i in range(n,0,-1):
    for j in range(n-i+1,n+1):

        if j == n or i==n or j == n-i+1:
            print(j, end=' ')
        else:
            print(' ', end=' ')

    print()