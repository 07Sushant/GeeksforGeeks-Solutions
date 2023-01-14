#User function Template for python3

from sortedcontainers import SortedList

class Solution():
    def countSubstring(self, S):
        s=SortedList()
        s.add(0)
        c=0
        ans=0
        for el in S:
            c+=1 if el=="1" else -1
            t=c-1
            ans+=s.bisect_right(t)
            s.add(c)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        print(Solution().countSubstring(s))
# } Driver Code Ends