

# https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/

from collections import deque

def largest(arr, k):

    dq = deque()
    ans = []

    for i in range(k):
        
        while dq and arr[dq[-1]] <= arr[i]:
            dq.popleft()
        
        dq.append(i)

    for i in range(k, len(arr)):
        ans.append(arr[dq[0]])
        
        # TODO: check if this is possible with if condition as well (bcos i think it is)
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()

        dq.append(i)

    return ans


arr = [12, 1, 78, 90, 57, 89, 56]
k = 3
print(largest(arr, k))