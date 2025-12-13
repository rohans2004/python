num = int( input('Enter number :'))     #take user input 
a = 0           #initializin  first digit  
b = 1           #initializin  second digit 
for i in range (num):
    print(a)            #printing a
    a , b = b , a + b           #changing the value building the logic 