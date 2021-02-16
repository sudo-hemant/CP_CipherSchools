
# https://practice.geeksforgeeks.org/problems/nth-fibonacci-number1335/1

def nthFibonacci (n, a = 0, b = 1):
    if n == 0:
        return a
    elif n == 1:
        return b
    return nthFibonacci(n - 1, b, a + b)


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        # ob = Solution()
        print(nthFibonacci(n))