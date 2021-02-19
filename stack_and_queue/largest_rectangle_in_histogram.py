
# https://leetcode.com/problems/largest-rectangle-in-histogram/


# NOTE:  Method 1 

# iterate over the histogram, find prev smaller and next smaller of the current bar
# and calculate the max sum 
# TC -- O(N ^ 2)


# ------------------------------------------------------------------------------------


# NOTE: Method 2 

# optimize the previous method , instead of findind the prev and next smaller element of 
# the current bar every time, we find the pev and next smaller element of every bar
# using the stack method in O(N) time and store it in the array


def largest(arr):

    if len(arr) == 1:
        return arr[0]

    previous_smaller = [0] * len(arr)
    next_smaller = [0] * len(arr)
    stack = []
    result = float('-inf')

    previous_smaller[0] = -1
    stack.append(0)
    for i in range(1, len(arr)):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        temp = stack[-1] if stack else -1
        previous_smaller[i] = temp
        stack.append(i)

    next_smaller[-1] = len(arr) 
    stack.append(len(arr) - 1)
    for i in reversed(range(len(arr) - 1)):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        temp = stack[-1] if stack else len(arr) 
        next_smaller[i] = temp
        stack.append(i)

    for i in range(len(arr)):
        result = max(result, arr[i] * (next_smaller[i] - previous_smaller[i] - 1))

    return result


# print(largest([ 2, 1, 5, 6, 2, 3 ]))
# print(largest([ 2, 4 ]))


# -------------------------------------------------------------------------------------


# NOTE: Method 3 

# the trick here is whenever we remove an element from stack our current element is the next 
# prev element and below the top of stack is the prev smaller element


def largest_histogram(arr):

    stack = []
    result = float('-inf')

    for i in range(len(arr)):
        while stack and arr[stack[-1]] >= arr[i]:
            popped = stack.pop()
            result = max(result, arr[popped] * (i - stack[-1] -1 if stack else i))

        stack.append(i)
    
    while stack:
        popped = stack.pop()
        result = max(result, arr[popped] * (len(arr) if not stack else len(arr) - stack[-1] - 1))
    
    print(result)


largest_histogram([ 2 ])


# -----------------------------------------------------------------------------------


# OR 
# TODO: DOUBT

def largest_histogram_MODIFIED(arr):

    arr.append(0)
    stack = [-1]
    result = 0  # for tc : [0]
    print(result)

    for i in range(len(arr)):

        # TODO: DOUBT WHY its not >= but only > ? 
        while arr[stack[-1]] > arr[i]:
            popped = stack.pop()
            
            # MODIFIED
            result = max(result, arr[popped] * (i - 1 - stack[-1]))

        stack.append(i)
        
    print(result)



largest_histogram_MODIFIED([ 2, 1, 5, 6, 2, 3 ])