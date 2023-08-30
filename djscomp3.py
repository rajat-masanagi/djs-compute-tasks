n=int(input("Enter number: "))
while(n<1900 or n>100000):
    n=int(input("Enter a number between 1900 and 10^5: "))
def leap(n):
    if(n%4==0):
        if(n%400==0):
            c=True
        elif(n%100==0):
            c=False
        else:
            c=True
    else:
        c=False
    return c
print(leap(n))
