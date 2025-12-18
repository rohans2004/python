        # 
      # # 
    # # # 
  # # # # 
# # # # # 
  # # # # 
    # # # 
      # # 
        # 


n = int(input("Enter Number : "))

for i in range(1,n+1):
   
   #for Spaces
   for  j in range(n-i):
      print(" " , end = ' ')
    
    #for star
   for k in range(i):
      print("#",end = ' ')
   print()

for i in range(n-1,0,-1):
   
   #for Spaces
   for  j in range(n-i):
      print(" " , end = ' ')
    
    #for star
   for k in range(i):
      print("#",end = ' ')
   print()