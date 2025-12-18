        # # # # 
      # # # # 
    # # # # 
  # # # # 


n = int(input('Enter Number :')) 
for row in range(n , 0 , -1 ):
    for  space in range (row):
        print(' ',end = ' ')
    for hash in range(1,n+1):
        print("#",end = ' ')
    print()