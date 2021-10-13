target=input()
t=list(target)
t1=[ord(i)-96 for i in t]
print(t1)
pos=1
for i in range(0,len(t)):
    
    if(pos>t1[i]):
        trav=pos-t1[i]
        for j in range(0,trav//5):
            print("u")
        j=j+1
        if(j*5>trav):
            for k in range(0,j*5-trav):
                print("l")
            print("!")
        elif(j*5<trav):
            for k in range(0,trav-j*5):
                print("r")
            print("!")
        else:
            print("!")
            
    elif(pos<t1[i]):
        trav=t1[i]-pos
        
        for j in range(0,trav//5):
            print("d")
        j=j+1
        if(j*5>trav):
            for k in range(0,j*5-trav):
                print("l")
            print("!")
        elif(j*5<trav):
            for k in range(0,trav-j*5):
                print("r")
            print("!")
        else:
            print("!")
    else:
        print("!")
    pos=t1[i]
