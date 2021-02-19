

# https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1/?track=DSASP-Stack&batchId=154


# NOTE:  Method -- 1

# push all n elements into the stack and process 2 elements at a time

# If A knows B, then A can't be a celebrity. Discard A, and B may be celebrity.
# If A doesn't know B, then B can't be a celebrity. Discard B, and A may be celebrity.
# Repeat above two steps till there is only one person.
# Ensure the remained person is a celebrity. (

def celebrity_stack(m):

    stack = []
    
    for i in range(len(m)):
        stack.append(i)

    while len(stack) > 1:
        a = stack.pop()
        b = stack.pop()

        if m[a][b] and m[b][a]:
            continue
        elif m[a][b]:
            stack.append(b)
        else:
            stack.append(a)
    
    if not stack:
        return -1

    candidate = stack.pop()

    for i in range(len(m)):
        if m[candidate][i] or (i != candidate and not m[i][candidate]):
            return -1

    return candidate


print(celebrity_stack([
    # [0, 0, 1, 0],
    # [0, 0, 1, 0],
    # [0, 0, 0, 0],
    # [0, 0, 1, 0]
    [0, 1],
    [1, 0]
]))


# ------------------------------------------------------------------------------


# NOTE:  USING Two-Pointer approach

# The idea is to use two pointers, one from start and one from the end. 
# Assume the start person is A, and the end person is B. If A knows B, 
# then A must not be the celebrity. Else, B must not be the celebrity. 
# At the end of the loop, only one index will be left as a celebrity. 
# Go through each person again and check whether this is the celebrity. 
# The Two Pointer approach can be used where two pointers can be assigned, 
# one at the start and other at the end and the elements can be compared 
# and the search space can be reduced


def celebrity_two_pointer(matrix):
    a, b = 0, len(matrix) - 1

    while a < b:
        if matrix[a][b]:
            a += 1
        else:
            b -= 1
    
    for i in range(len(matrix)):
        if matrix[a][i] or (i != a and not matrix[i][a]):
            return -1
    
    return a


print(
    celebrity_two_pointer([
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0]
        # [0, 1],
        # [1, 0]
    ])
)
