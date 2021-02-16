
# https://www.geeksforgeeks.org/find-possible-words-phone-digits/


def find_possible_combinations(number):
    
    result = []
    hash_number = [ "", "", 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz' ]
    temp = []

    util(0, temp, len(number), number, result, hash_number)

    return result


def util(index, temp, n, number, result, hash_number):
    # base case
    if index >= n:
        ans = ''.join(temp)
        result.append(ans)
        return

    curr_no = number[index]

    possible_char = hash_number[int(curr_no)]

    for char in possible_char:
        temp.append(char)
        
        util(index + 1, temp, n, number, result, hash_number)

        temp.pop()


tc = int(input())

for _ in range(tc):
    number = input()

    print(find_possible_combinations(number))