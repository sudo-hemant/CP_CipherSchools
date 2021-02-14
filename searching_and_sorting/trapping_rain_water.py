
# https://leetcode.com/problems/trapping-rain-water/


class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        
        if len(height) < 3:
            return 0
        
        tallest_pos, ans = -1, 0
        left, right = 0, length-1
        
        tallest_pos = self.tallest(height)

        for i in range(1, tallest_pos):
            if height[i] >= height[left]:
                left = i
            else:
                ans += height[left] - height[i]
        print(ans)
        for i in range(length-2, tallest_pos, -1):
            if height[i] >= height[right]:
                right = i
            else:
                ans += height[right] - height[i]
        print(ans)     
        return ans
        

    def tallest(self, height):
        tallest_pos = 0
        for i in range(len(height)):
            if height[i] > height[tallest_pos]:
                tallest_pos = i
        print(tallest_pos)
        return tallest_pos