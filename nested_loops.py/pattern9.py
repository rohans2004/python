            # # # # # 
          # # # # # 
        # # # # # 
      # # # # # 
    # # # # # 
  # # # # # 

n = int ( input('Enter Number : '))
for row in range(n):
    for i in range(n-row):
        print(" ", end= ' ')
    for j in range(n):
        print("#",end = ' ')
    print()