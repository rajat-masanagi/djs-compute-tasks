N=int(input("Enter a number: "))
l=[]
def fib(n):
    if(n>2):
        l.append(0)
        l.append(1)
        for i in range(2,n):
            l.append(l[i-1]+l[i-2])
fib(N)
cube=list(map(lambda x:x*x*x,l))
print(cube)
