n = int (input('Enter number :'))
# # # # # 
  # # # # # 
    # # # # # 
      # # # # # 
        # # # # # 
for row in range (n):

    for space in range(row):
        print(' ' , end = ' ' )
    for hash in range(1,n+1):
        print("#",end = ' ')
    print()