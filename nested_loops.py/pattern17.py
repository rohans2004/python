        # 
      # # # 
    # # # # # 
  # # # # # # # 
# # # # # # # # # 
  # # # # # # # 
    # # # # # 
      # # # 
        # 

n = int (input('Enter number : '))

for i in range(1,n+1):
    for space in range (n - i):
        print(" " , end = ' ')
    for star in range(2*i - 1 ):
        print("#", end = ' ')
    print()

for i in range(1,n):
    for space in range(i):
        print(" ", end=" ")

    for star in range(2*(n - i) - 1):
        print("#", end=" ")
    print()