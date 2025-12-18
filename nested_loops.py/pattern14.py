# # # # # # # # # 
  # # # # # # # 
    # # # # # 
      # # # 
        # 


n = int(input("Enter number: "))

for i in range(n):
    # spaces
    for space in range(i):
        print(" ", end=" ")

    # stars
    for star in range(2*(n - i) - 1):
        print("#", end=" ")

    print()
