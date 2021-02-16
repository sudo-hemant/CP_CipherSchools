
# https://www.geeksforgeeks.org/count-possible-decodings-given-digit-sequence/


def count_ways(str):
    result = []
    temp = []
    hash_map = [ '', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

    util(0, len(str), str, temp, result, hash_map)

    print(result)
    

def util(index, n, str, temp, result, hash_map):
    # base case
    if index >= n:
        ans = ''.join(temp)
        result.append(ans)
        return


    curr_num = str[index]
    
    if curr_num == '0':
        return
    
    curr_char = hash_map[int(curr_num)]

    temp.append(curr_char)
    util(index + 1, n, str, temp, result, hash_map)
    temp.pop()

    if index + 1 >= n:
        return

    next_num = str[index + 1]
    next_char = curr_num + next_num

    if int(next_num) <= 26:
        next_char = hash_map[int(next_char)]

        temp.append(next_char)
        util(index + 2, n, str, temp, result, hash_map)
        temp.pop()


    
tc = int(input())

for _ in range(tc):
    number = input()

    count_ways(number)
    