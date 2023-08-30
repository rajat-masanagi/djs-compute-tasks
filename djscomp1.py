n=int(input("Enter number: "))
while(n<1 or n>100):
    n=int(input("Enter a number between 1 and 100: "))
if(n%2!=0):
    print("Weird")
elif(n>=2 and n<=5):
    print("Not Weird")
elif(n>=6 and n<=20):
    print("Weird")
elif(n>20):
    print("Not Weird")

