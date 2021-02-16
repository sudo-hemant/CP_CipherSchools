# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        cache = [[0 for j in range(n)] for i in range(m)]
        
        for row in range(m):
            cache[row][0] = 1
        for column in range(n):
            cache[0][column] = 1
            
        for i in range(1, m):
            for j in range(1, n):
                cache[i][j] = cache[i][j - 1] + cache[i - 1][j]
        
        return cache[-1][-1]