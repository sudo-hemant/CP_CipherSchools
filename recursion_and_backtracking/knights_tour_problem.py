

def knight_tour(n):

    is_visited = [ [-1 for _ in range(n)] for _ in range(n) ]
    position = 0
    x_pos = [-1, -2, -2, -1, 1, 2, 2, 1]
    y_pos = [-2, -1, 1, 2, 2, 1, -1, -2]

    is_visited[0][0] = 0

    knight_tour_util(0, 0, 1, is_visited, n, x_pos, y_pos)

    print(is_visited)



def knight_tour_util(x, y, position, is_visited, n, x_pos, y_pos):
    # base case
    if position == n ** 2:
        return True

    for k in range(8):
        new_x = x + x_pos[k]
        new_y = y + y_pos[k] 

        if is_safe(new_x, new_y, is_visited, n):
            is_visited[new_x][new_y] = position

            if knight_tour_util(new_x, new_y, position + 1, is_visited, n, x_pos, y_pos):
                return True

            is_visited[new_x][new_y] = -1

    return False


def is_safe(a, b, is_visited, n):
    if a >= 0 and b >= 0 and a < n and b < n and is_visited[a][b] == -1:
        return True
    return False


if __name__ == '__main__':
    tc = int(input())

    for _ in range(tc):
        n = int(input())
        knight_tour(n)