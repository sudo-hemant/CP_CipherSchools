
# https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/


def ispar(s):
    stack = []
    
    for brace in s:
        if brace == '{' or brace == '[' or brace == '(':
            stack.append(brace)
        elif brace == '}':
            if not stack or stack[-1] != '{':
                return False
            else:
                stack.pop()
        elif brace == ']':
            if not stack or stack[-1] != '[':
                return False
            else:
                stack.pop()
        elif brace == ')':
            if not stack or stack[-1] != '(':
                return False
            else:
                stack.pop()
                
    return False if stack else True
            


# -------------------------------------------------------------


# NOTE: better method

def ispar_2(x):
    stack = []
    mp = { '}' : '{', ']' : '[', ')' : '(' }
    
    for brace in s:
        if brace in [ '[', '{', '(' ]:
            stack.append(brace)
        else:
            opposite_pair = mp[brace]
            
            if not stack or stack[-1] != opposite_pair:
                return False
            else:
                stack.pop()
                
    return False if stack else True
    