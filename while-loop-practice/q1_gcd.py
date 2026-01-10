a = int(input("Enter a :"))
b = int(input("Enter b :"))
if a>b:
    max = a
else:
    max = b
i = max-1
while(i!=0):
    if a%i==0 and b%i==0:
        print(f"Grand Common Divisor of {a} abd {b} is :{i}")
        break
    i-=1