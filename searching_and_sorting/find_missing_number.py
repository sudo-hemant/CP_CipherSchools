
# https://leetcode.com/problems/missing-number/


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        total = (l * (l+1)) // 2
        return total - sum(nums) 