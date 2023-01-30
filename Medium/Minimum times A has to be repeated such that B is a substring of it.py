#User function Template for python3

class Solution:
    def minRepeats(self, A, B):
        rep=A
        count=1
        while len(rep)<len(B):
            count+=1
            rep+=A
            
        if B in rep:
            return count
            
        rep+=A
        if B in rep:
            return count+1
            
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A=input()
        B=input()
        
        ob = Solution()
        print(ob.minRepeats(A,B))
# } Driver Code Ends