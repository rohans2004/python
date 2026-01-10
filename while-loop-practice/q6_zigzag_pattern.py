n = int(input('enter '))

for i in range(1,n-5):
    if i%2==0:
        for j in range(1,n-3):
            if j%2==0:
                print('*',end = ' ')
            else:
                print(' ',end =' ')
        print('')
    else:
        for j in range(1,n-3):
            if j%2!=0:
                print("*",end = ' ')
            else:
                print(" ",end = ' ')
        print('')


My Method same Question:-

n= int(input("Enter Number : "))
for row in range(1,n-2):
    for col in range(1,n):
        if(row+col)%2==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
