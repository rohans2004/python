num  = int(input('Enter number :')) #take user input 
a , b = 0 , 1                       #initializin  first and second digit
print(f'Fibbonachi series is :' , end = ' ')
while (num  > 0 ):
    print(a , end = ' ')            #printing a
    a ,b = b , a + b                #changing the value building the logic 
    num -= 1