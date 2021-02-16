
# https://practice.geeksforgeeks.org/problems/largest-number-in-k-swaps-1587115620/1#


def findMaximumNum(s, k):

    number = list(s)
    find_max_util.maximum = number[:]
    
    find_max_util(number, k)
    
    return int(''.join(find_max_util.maximum))
    
    
def find_max_util(number, k):
    # base case
    if k == 0:
        return
    
    for i in range(len(number) - 1):
        for j in range(i + 1, len(number)):
            
            if number[i] < number[j]:
                number[i], number[j] = number[j], number[i]
                
                if number > find_max_util.maximum:
                    find_max_util.maximum = number[:]

                find_max_util(number, k - 1)
                
                number[i], number[j] = number[j], number[i]



if __name__=="__main__":
    for _ in range(int(input())):
        k = int(input())
        s = input()
        print(findMaximumNum(s,k))
