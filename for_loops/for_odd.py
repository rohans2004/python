#printing odd number from 1 to 10 
for i in range( 1 , 11 , 1 ):
    if i%2 != 0 :
        print(i)

#printing odd number from 10 to 1. in reverse  
for i in range(10 , 0 , -1 ):   #running the loop in inverse
    if i%2 != 0 :
        print(i)

#priting odd number by taking range from the user 
start = int(input('Enter the starting point :'))    #input start point here 

end = int(input('Enter the ending point :'))        #input ending point here 

if start > end :

    for i in range (end , start + 1 , 1):

        if i%2 !=0 :

            print(i)

else :

    for i in range (start , end + 1 , 1 ):

        if i%2 != 0 :
            
            print(i)