
# https://practice.geeksforgeeks.org/problems/solve-the-sudoku-1587115621/1/?track=DSASP-Backtracking&batchId=154


from math import sqrt

def solve_sudoku(sudoku):
    
    def sudoku_helper(i, j, sudoku):
        if i == len(sudoku):
            return True
        
        ni, nj = i, j + 1
        if nj == len(sudoku):
            ni, nj = i + 1, 0
        
        if sudoku[i][j]:
            if sudoku_helper(ni, nj, sudoku):
                return True
            else:
                return False
        else:
            for possible_no in range(1, 10):
                if is_safe(i, j, possible_no, sudoku):
                    sudoku[i][j] = possible_no    
                    if sudoku_helper(ni, nj, sudoku):
                        return True
                    sudoku[i][j] = 0
        return False
        
        
    if sudoku_helper(0, 0, sudoku):
        return True
    return False
    

def is_safe(x, y, possible_no, sudoku):
    
    for i in range(9):
        if sudoku[x][i] == possible_no:
            return False
        if sudoku[i][y] == possible_no:
            return False
    
    size = sqrt(len(sudoku))
    x = int(x // size * size)
    y = int(y // size * size)
    
    for i in range(3):
        for j in range(3):
            if sudoku[x + i][y + j] == possible_no:
                return False
    return True
    
    
def print_grid(arr):
    
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=" ")
    print()




if __name__=="__main__":
    t = int(input())
    while(t>0):
        grid = [[0 for i in range(9)] for j in range(9)]
        row = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(9):
            for j in range(9):
                grid[i][j] = row[k]
                k+=1
            
        if(solve_sudoku(grid)==True):
            print_grid(grid)
        else:
            print("No solution exists")
        t = t-1
