
def permutations(start, end, str):
    if start == end:
        print(''.join(str))

    for curr in range(start, end):
        str[start], str[curr] = str[curr], str[start]
        permutations(start + 1, end, str)
        str[start], str[curr] = str[curr], str[start]


tc = int(input())

for _ in range(tc):
    str = list(input())

    permutations(0, len(str), str)