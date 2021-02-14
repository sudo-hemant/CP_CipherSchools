
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.firstOccurence(nums, target)
        
        if first == -1:
            return [-1, -1]
        if first == len(nums) - 1:
            return [first, first]
        
        last = self.lastOccurence(nums, first, target)
        return [first, last]
        
    
    def firstOccurence(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if mid == 0 and nums[mid] == target:
                return mid
                            
            if nums[mid] == target:
                if nums[mid - 1] == target:
                    r = mid - 1
                else:
                    return mid
            elif target < nums[mid]:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
                
        return -1
    
    
    def lastOccurence(self, nums, start, target):
        l, r = start, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if mid == len(nums) - 1 and nums[mid] == target:
                return mid
            
            if nums[mid] == target:
                if nums[mid + 1] == target:
                    l = mid + 1
                else:
                    return mid
            elif target < nums[mid]:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
                
        return -1