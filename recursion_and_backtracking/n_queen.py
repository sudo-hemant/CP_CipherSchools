
# https://practice.geeksforgeeks.org/problems/n-queen-problem0315/1#

class Solution:
    def nQueen(self, n):
    
        is_visited = [ [False] * n for _ in range(n) ]
        result = []
        
        self.n_queen_util(0, n, is_visited, result)
        result.sort()
        
        return result
        
        
    def n_queen_util(self, column, n, is_visited, result):
        # base case
        if column >= n:
            temp = []
            
            for i in range(n):
                for j in range(n):
                    if is_visited[i][j]:
                        temp.append(j + 1)
                        break
            result.append(temp)
            
        for i in range(n):
            if self.is_safe(i, column, n, is_visited):
                is_visited[i][column] = True
                self.n_queen_util(column + 1, n, is_visited, result)
                is_visited[i][column] = False
    
    
    def is_safe(self, row, col, n, is_visited):
        
        # check current row upto its left side
        for j in range(col):
            if is_visited[row][j]:
                return False
                
        # left diagonal
        # for i, j in zip(reverse(range(row)), reverse(range(col))):
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if is_visited[i][j]:
                return False
                
        # lower right diagonal
        # for i, j in zip(range(row, n), reverse(range(col))):
        for i, j in zip(range(row, n), range(col, -1, -1)):
            if is_visited[i][j]:
                return False
                
        return True


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()