# This is 0 1 Knapsack Using recurssion and Top Down Approach

'''
Example : 

Input :

n = 3
W = 4
val[] = {1,2,3}
wt[] = {4,5,1}

Output : 3
'''

def knapSack_Top_Down(self,W, wt, val, n): 

    t=[ [ 0 for i in range(W+1) ] for j in range(len(wt)+1) ]
    for i in range(1,len(t)):
        for j in range(1,len(t[0])):
            if i==0 or j==0:
                t[i][j]=0
            if j>=wt[i-1]:
                t[i][j]=max(  val[i-1]+t[i-1][j-wt[i-1]],t[i-1][j]     )
            else:
                t[i][j]=t[i-1][j]
    return t[len(wt)][W]


def knapSack_Recurssion(self,W, wt, val, n):

    if n==0 or W==0:
      return 0
    
    if wt[n-1]<=W:
        return max(val[n-1]+self.knapSack(W-wt[n-1],wt,val,n-1)     , self.knapSack(W,wt,val,n-1)        )
    
    else:
        return self.knapSack(W,wt,val,n-1)    