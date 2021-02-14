
# https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1#

def minimumPlatform(n, arr, dep):
    '''
    :param n: number of activities
    :param arr: arrival time of trains
    :param dep: corresponding departure time of trains
    :return: Integer, minimum number of platforms needed
    '''

    arr.sort()
    dep.sort()
    
    current_platforms = minimum_platforms = 1
    i, j = 1, 0
    
    while i < n and j < n:
        if dep[j] < arr[i]:
            current_platforms -= 1
            j += 1
        else:
            current_platforms += 1
            i += 1
            
        minimum_platforms = max(current_platforms, minimum_platforms)
        
    return minimum_platforms
