
# https://leetcode.com/problems/excel-sheet-column-number/
    

class Solution:
    def titleToNumber(self, s: str) -> int:
        length = len(s)
        ans = 0
        
        for i in range(length):
            cha = ord(s[i]) % 64
            ans += (26 ** (length -i-1)) * cha
        
        return ans