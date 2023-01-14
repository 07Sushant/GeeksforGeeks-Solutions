#User function Template for python3
class Solution:
    def isPowerofTwo(self,n):
        while (n>1):
            n = n/2
        if (n==1):
            return True
        return False
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        if ob.isPowerofTwo(n):
            print("YES")
        else:
            print("NO")
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends