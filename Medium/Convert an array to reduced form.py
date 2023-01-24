#User function Template for python3
class Solution:

    def convert(self,arr, n):
        # code here
        new = [(arr[i],i) for i in range(n)]
        dit = {}
        new.sort()
        i=0
        for a,b in new:
            dit[a] = i
            i+=1
        
        for i in range(n):
            arr[i] = dit[arr[i]]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.convert(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
