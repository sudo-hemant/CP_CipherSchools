
# https://leetcode.com/problems/search-in-rotated-sorted-array/


class Solution:
    def search(self, arr: List[int], target: int) -> int:
        low, high = 0, len(arr) - 1
        
        while low <= high:
            mid = (low+high) // 2
            
            if arr[mid] == target:
                return mid
            elif arr[low] <= arr[mid]:
                if arr[low] <= target <= arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            
            elif arr[mid] <= arr[high]:            
                if arr[mid] <= target <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1