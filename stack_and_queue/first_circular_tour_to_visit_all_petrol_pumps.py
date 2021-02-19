
def tour(arr, n):

    start, end = 0, 1
    curr_petrol = arr[start][0] - arr[start][1]
    
    while start != end or curr_petrol < 0:
        while curr_petrol < 0 and start != end:
            curr_petrol -= arr[start][0] - arr[start][1]
            start = (start + 1) % n
            
            if start == 0:
                return -1
                
        curr_petrol += arr[end][0] - arr[end][1]
        end = (end + 1) % n
        
    return start
    
