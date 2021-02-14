
# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        curr_max, count = nums[0], 1

        for i in range(1, len(nums)):
            if count == 0:
                count += 1
                curr_max = nums[i]
            elif nums[i] == curr_max:
                count += 1
            else:
                count -= 1

        return curr_max 