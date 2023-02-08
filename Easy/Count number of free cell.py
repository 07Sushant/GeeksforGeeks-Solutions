class Solution():
    def countZero(self, n, k ,arr):
        total, visit_row, visit_col, ans = n*n, set(), set(), []

        for r,c in arr:

            visit_row.add(r)

            visit_col.add(c)

            ans.append(total - len(visit_row)*n - len(visit_col)*(n-(len(visit_row))))

        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(int(input())):
    n,k=map(int,input().split())
    arr = []
    for i in range(k):
        x,y=map(int,input().split())
        arr.append([x, y])
    obj = Solution()
    res = obj.countZero(n, k, arr)
    for i in res:
        print(i,end = " ")
    print()
# } Driver Code Ends