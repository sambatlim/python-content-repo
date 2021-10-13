numRows=int(input())
l=[]

l.append([1])
for i in range(1,numRows):
    print(l)
    k=[]
    k.append(1)
    for j in range(1,i+1):
            
            
        if(j-1==i-1):
            k.append(l[i-1][j-1])
        else:
            k.append(l[i-1][j-1]+l[i-1][j])
    l.append(k)
print(l)
        
