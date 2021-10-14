# longest_common_subsequence is function to find lcs between 2 arrays or strings

def longest_common_subsequence(self,s1,s2):
    if len(s1)==0 or len(s2)==0:
        return 0

    x=len(s1)
    y=len(s2)
    
    mm=[[0 for k in range(y+1)] for l in range(x+1)]
    
    for i in range(1,len(mm)):
        for j in range(1,len(mm[0])):
            
            if s1[i-1]==s2[j-1]:
                mm[i][j]=1+mm[i-1][j-1]
            else:
                mm[i][j]=max(mm[i-1][j],mm[i][j-1])
            
          
    return int(mm[i][j])