
# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if len(matrix) == 0:
            return []
        
        i, j, k, l = 0, len(matrix[0]) -1, len(matrix) -1, 0
        ans = []*(len(matrix) * len(matrix[0]))
        
        while i <= k and l <= j:
            for right in range(l, j+1):
                ans.append(matrix[i][right])
            i += 1
            
            for down in range(i, k+1):
                ans.append(matrix[down][j])
            j -= 1

            if i > k:
                break           
            
            for left in range(j, l-1, -1):
                ans.append(matrix[k][left])
            k -= 1
            
            if l > j:
                break            
            
            for top in range(k, i-1, -1):
                ans.append(matrix[top][l])
            l += 1
                       
        return ans