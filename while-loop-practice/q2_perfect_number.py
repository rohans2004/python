n = int(input('Enter number :'))
sum = 0
i = 1
while(i<n):
    if n%i==0:
        sum+=i
    i+=1
if sum == n :
    print(f"the number {n} is PERFECT NUMBER.")
else:
    print(f"the number {n} is NOT a PERFECT NUMBER.")