
# https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1


def merge(arr_1,arr_2,n,m):

    maximum = max(arr_1[-1], arr_2[-1]) + 1

    i = j = k = 0

    while i < n and j < m:
        
        e1 = arr_1[i] % maximum
        e2 = arr_2[j] % maximum

        if e1 <= e2:
            if k < n:
                arr_1[k] += (e1 * maximum)
            else:
                arr_2[k - n] += (e1 * maximum)
            
            i = i + 1

        else:
            if k < n:
                arr_1[k] += (e2 * maximum)
            else:
                arr_2[k - n] += (e2 * maximum)

            j = j + 1

        k += 1

    # process those elements which are left in array 1
    while i < n:
        el = arr_1[i] % maximum

        if k < n:
            arr_1[k] += (el * maximum)
        else:
            arr_2[k - n] += (el * maximum)
        
        i, k = i + 1, k + 1
    
    # process those elements which are left in array 2
    while j < m:
        el = arr_2[j] % maximum

        if k < n:
            arr_1[k] += (el * maximum)
            or
            arr_2[k] += (el * maximum)
        else:
            arr_2[k - n] += (el * maximum)

        j, k = j + 1, k + 1

    for i in range(n):
        arr_1[i] = arr_1[i] // maximum
        
    for j in range(m):
        arr_2[j] = arr_2[j] // maximum

