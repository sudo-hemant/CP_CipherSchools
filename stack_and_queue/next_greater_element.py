




def nextLargerElement(arr,n):
    
    stack = []
    result = [0] * n
    
    for i in reversed(range(n)):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        
        if not stack:
            result[i] = -1
        else:
            result[i] = stack[-1]
        stack.append(arr[i])
        
    return result
