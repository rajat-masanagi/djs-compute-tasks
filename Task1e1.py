n,s=(int(x) for x in input("Enter number of students and subjects: ").split())
L=[]
A=[]
for i in range(0,n):
    T=list(map(int,input().split()))
    L.append(T)
    sum=0
    for j in T:
        sum=sum+j
        A.append(sum/s)        
result=zip(L,A)
print(list(result))
