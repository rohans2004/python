# # *               
# # * *             
# # *   *           
# # *     *         
# # *       *       
# # *         *     
# # *           *   
# # * * * * * * * * 

# n = int (input("ENTER NUMBER : "))

# for i in range( 1 , n+1):
#     for j in range(1, n+1):
#         if  i == n or i == j or j == 1 :
#             print("*",end = ' ')
#         else:
#             print(" ",end = ' ')
#     print()



#             * 
#           * * 
#         *   * 
#       *     * 
#     *       * 
#   *         * 
# * * * * * * * 

# n = int (input("ENTER NUMBER : "))

# for i in range( 1 , n+1):
#     for j in range(1, n+1):
#         if  i == n or j == n or i + j == n+1 :
#             print("*",end = ' ')
#         else:
#             print(" ",end = ' ')
#     print()

# for i in range( 1 , n+1):
#     for j in range(1, n+1):
#         if  i == n or j == n or j == 1 or i + j == n+1 or i ==1 :
#             print("*",end = ' ')
#         else:
#             print(" ",end = ' ')
#     print()

# n = 4

# for row in range (n):

#     for space in range(row):
#         print(' ' , end = ' ' )
#     for hash in range(1,n+1):
#         print("#",end = ' ')
#     print()

# # # # # # 
# # # # # 
# # # # 
# # # 
# # 
# 
# # 
# # # 
# # # # 
# # # # # 
# # # # # # 

# for i in range (n , 0 , -1):
#     for j in range(i):
#         print('#',end = ' ')
#     print()
# for i in range(1,n+1):
#     for j in range(i):
#         print("#",end = ' ')
#     print()


              # 
            #   # 
          #       # 
        #           # 
      #               # 
    #                   # 
  # # # # # # # # # # # # # 

# n = int (input('Enter number : ' ))
# for i in range (n):
    
#     for j in range ( n - i ):
#         print(' ' , end=' ')
#     for j in range ( 2 * i - 1 ):
#         if j == 0 or i == n - 1 or j == 2*i -2 :
#             print("#",end = ' ')
#         else:
#             print(" ",end = ' ')
#     print()



# n = 5 

# for i in range(1,n+1):
#     for j  in range(n-i):
#         print(" ",end = ' ')
#     for j in range(2 * i- 1 ):
#         print( ,end = ' ')
#     print()





# n = 4 
# temp = 0 
# temp1 = 2 
# for i in range(1 ,n+1 ):
#     temp += 1                   
#     for j in range(n - i ):
#         print(' ' , end = ' ')
#     for  j in range(temp , temp + i ):
#         print(j , end = ' ')

#     for k in range ( 1,i ):
#         print(temp1,end = ' ')
#         temp1+=1
    
#     print()
















# n=5

# for i in range (n,0,-1):
#     # for j in range(i):
#     #     print("_",end = ' ')
#     for s in range(n , 0 -1 ):
#         print("#",end = ' ')
#     print()