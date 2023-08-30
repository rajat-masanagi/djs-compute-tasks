n=int(input("Enter number: "))
while(n<1 or n>20):
    n=int(input("Enter a number between 1 and 20: "))
for i in range(n):
    print(i*i)
