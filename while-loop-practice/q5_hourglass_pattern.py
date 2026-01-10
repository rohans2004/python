n = int(input('enter numbr :')) 
temp = n * 2 - 1
for i in range(n):
    for spc in range(i):
        print(' ',end =' ')
    for j in range(temp):
        print('*',end = ' ')
    temp-=2
    print('')
temp2 = 3 
for  i in range(n-2,-1,-1):
    for spc in range(i):
        print(' ',end =' ')
    for j in range(temp2):
        print("*",end=' ')
    temp2+=2
    print('')