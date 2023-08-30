list=[]
N=int(input("Enter N: "))

for i in range(N):
    n=int(input("1:Insert\n2:Print\n3:Remove\n4:Append\n5:Sort\n6:Pop\n7:Reverse\n0:Exit\n"))
    if(n==4):
        x=int(input("Enter number to be appended: "))
        list.append(x)      
    if(n==1):
        p=int(input("Enter number to be inserted: "))
        k=int(input("Enter position: "))
        for i in range(len(list),k-1,-1):
            list[i]=list[i-1]
        list[k-1]=p        
    if(n==2):
        for i in list:
            print(i," ")        
    if(n==3):
        m=int(input("Enter number to be deleted: "))
        for i in range(len(list)):
            if(i>=list.index(m) and i!=(len(list)-1)):
                list[i]=list[i+1]
        list.pop()      
    if(n==5):
        for i in range(len(list)-1):  
            for j in range(len(list)-1):  
                if(list[j]>list[j+1]):  
                    temp = list[j]  
                    list[j] = list[j+1]  
                    list[j+1] = temp        
    if(n==6):
        list.pop()        
    if(n==7):
        if(len(list)%2!=0):
            for i in range(int((len(list)+1)/2)):
                temp = list[i]  
                list[i] = list[len(list)-1-i]  
                list[len(list)-1-i] = temp
        else:
            for i in range(int(len(list)/2)):
                temp = list[i]  
                list[i] = list[len(list)-1-i]  
                list[len(list)-1-i] = temp
        




    
