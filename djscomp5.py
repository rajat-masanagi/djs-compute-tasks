import numpy as np
w=input("Enter array with spaces: ")
w.strip()
l=w.split(" ")
def arrays(arr):
    a=np.array(arr,float)
    if(len(a)%2!=0):
            for i in range(int((len(a)+1)/2)):
                temp = a[i]  
                a[i] = a[len(a)-1-i]  
                a[len(a)-1-i] = temp
    else:
        for i in range(int(len(a)/2)):
            temp = a[i]  
            a[i] = a[len(a)-1-i]  
            a[len(a)-1-i] = temp
    print(a)
arrays(l)