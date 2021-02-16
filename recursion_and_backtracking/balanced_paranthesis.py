

# https://practice.geeksforgeeks.org/problems/generate-all-possible-parentheses/1#


def AllParenthesis(n):
    result = []
    temp = []
    
    paranthesis_util(0, 0, temp, n, result)
    
    return result
    
    
def paranthesis_util(open, close, temp, n, result):
    if open > n or close > n or close > open:
        return 
    elif open == n and close == n:
        valid_pairs = ''.join(temp)
        result.append(valid_pairs)
        return
    
    temp.append('(')
    
    paranthesis_util(open + 1, close, temp, n, result)
    
    temp.pop()
    temp.append(')')
    
    paranthesis_util(open, close + 1, temp, n, result)
    
    temp.pop()



if __name__=="__main__":
    t=int(input())
    for i in range(0,t):
        n=int(input())
        result=AllParenthesis(n)
        result.sort()
        for i in range(0,len(result)):
            print(result[i])
        