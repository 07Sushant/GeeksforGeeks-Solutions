class Solution:

    def checkTriplet(self,a, n):
        a.sort()
        flag = False
        for i in range(0,len(a)-2):
            for j in range(i+1,len(a)-1):
                if (a[i]*a[i]+a[j]*a[j])**0.5 in a:
                    flag=True
                    break
            if flag==True:
                break
        return flag
#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.checkTriplet(arr, n)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends
# SUSHANT
