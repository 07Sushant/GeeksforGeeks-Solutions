#User function Template for python3

class Solution:
    def minVal(self, a, b):
        setBits=str(bin(b)).count("1")
        setBits1=str(bin(a)).count("1")
        ans = 0
        for i in range(32):
            mask=1<<i
            set=a&mask
            if set==0 and setBits>setBits1:
                ans|=mask
                setBits-=1
            elif set!=0 and setBits1>setBits:
                setBits1-=1
            else:
                ans|=set
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a = int(input())
        b = int(input())
        
        ob= Solution()
        print(ob.minVal(a,b))
# } Driver Code Ends