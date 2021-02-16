
# https://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/

class Solution:
    def trailingZeroes(self, N):
    	ans = 0
    	
    	while N >= 5:
    	    N //= 5
    	    ans += N
    	    
    	return ans



if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input()) 
        ob = Solution()
        ans = ob.trailingZeroes(N)
        print(ans)