#User function Template for python3

class Solution:

    #Function to perform case-specific sorting of strings.
    def caseSort(self,s,n):
        #code here
        l=[]
        r=[]
        for i in s:
            if i.upper()==i:
                l.append(i)
            else:
                r.append(i)
        l.sort()
        r.sort()
        p=len(l)
        q=len(r)
        ans=""
        i=j=0
        for k in s:
            if k.upper()==k:
                ans+=l[i]
                i+=1
            else:
                ans+=r[j]
                j+=1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        s=str(input())
        print(Solution().caseSort(s,n))
# } Driver Code Ends