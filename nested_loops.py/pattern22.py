n = int(input('Enter number : '))
        # 
      #   # 
    #       # 
  #           # 
#               # 
  #           # 
    #       # 
      #   # 
        # 


# Upper part
for i in range(1, n+1):
    for space in range(n - i):
        print(" ", end=' ')

    for star in range(2*i - 1):
        # 🔑 Hollow logic
        if star == 0 or star == 2*i - 2:
            print("#", end=' ')
        else:
            print(" ", end=' ')
    print()

# Lower part
for i in range(1, n):
    for space in range(i):
        print(" ", end=' ')

    for star in range(2*(n - i) - 1):
        # 🔑 Hollow logic
        if star == 0 or star == 2*(n - i) - 2:
            print("#", end=' ')
        else:
            print(" ", end=' ')
    print()


#         A 
#       A   C 
#     A       E 
#   A           G 
# A               I 
#   A           G 
#     A       E 
#       A   C 
#         A 


# Upper part
for i in range(1, n+1):
    for space in range(n - i):
        print(" ", end=' ')

    for star in range(2*i - 1):
        # 🔑 Hollow logic
        if star == 0 or star == 2*i - 2:
            print(chr(65+star), end=' ')
        else:
            print(" ", end=' ')
    print()

# Lower part
for i in range(1, n):
    for space in range(i):
        print(" ", end=' ')

    for star in range(2*(n - i) - 1):
        # 🔑 Hollow logic
        if star == 0 or star == 2*(n - i) - 2:
            print(chr(65+star), end=' ')
        else:
            print(" ", end=' ')
    print()
