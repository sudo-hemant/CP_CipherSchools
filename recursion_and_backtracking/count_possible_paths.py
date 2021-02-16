
def possbile_path(m, n):
    if m == 1 or n == 1:
        return 1

    return possbile_path(m - 1, n) + possbile_path(m, n - 1)


print(possbile_path(3, 3))