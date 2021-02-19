

def previous_smaller(arr, n):
    stack = []
    result = [0] * n

    for i in range(n):
        while stack and stack[-1] >= arr[i]:
            stack.pop()

        result[i] = stack[-1] if stack else -1
        stack.append(arr[i])

    return result


print(previous_smaller( [1, 6, 4, 10, 2, 5], 6 ))