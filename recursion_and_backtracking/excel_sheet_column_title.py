
# https://leetcode.com/problems/excel-sheet-column-title/

class Solution:
    def convertToTitle(self, n: int) -> str:
        result = []

        while n > 0:
            result.append(chr( (n - 1) % 26 + ord('A') ))
            n = (n - 1) // 26
            
        result.reverse()
        return ''.join(result)