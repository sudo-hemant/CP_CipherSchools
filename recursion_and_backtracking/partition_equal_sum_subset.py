
# https://practice.geeksforgeeks.org/problems/subset-sum-problem2014/1#


class Solution:
    def equalPartition(self, N, arr):
        total_sum = sum(arr)

        if total_sum % 2:
            return 0
        
        return self.is_possible(0, len(arr), arr, total_sum // 2)
        
    
    def is_possible(self, index, n, arr, target_sum):
        
        if index >= n:
            if not target_sum:
                return True
            return False
        
        if self.is_possible(index + 1, n, arr, target_sum - arr[index]):
            return True
        
        return self.is_possible(index + 1, n, arr, target_sum)



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")