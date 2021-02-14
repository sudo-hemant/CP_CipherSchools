
# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

def maxSubArraySum(a,size):
    
    curr_sum, max_so_far = a[0], a[0]
    
    for i in range(1, len(a)):
        a[i] = max(a[i], a[i] + a[i - 1])
        max_so_far = max(max_so_far, a[i])
    
    return max_so_far

