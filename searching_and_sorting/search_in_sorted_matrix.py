

# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not len(matrix) or not len(matrix[0]):
            return False
        
        if target < matrix[0][0] or matrix[-1][-1] < target:
            return False
        
        return self.row_search(matrix, target)
        
    
    def row_search(self, matrix, target):
        
        low, high = 0, len(matrix) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if matrix[mid][0] <= target and target <= matrix[mid][len(matrix[0]) - 1]:
                return self.column_search(mid, matrix, target)
            
            elif target < matrix[mid][0]: 
                high = mid - 1
                
            elif matrix[mid][0] < target:
                low = mid + 1
        
        return False
    
    
    def column_search(self, row, matrix, target):
        
        low, high = 0, len(matrix[0]) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if matrix[row][mid] == target:
                return True
            
            elif target < matrix[row][mid]:
                high = mid - 1
            
            elif matrix[row][mid] < target:
                low = mid + 1
        
        return False