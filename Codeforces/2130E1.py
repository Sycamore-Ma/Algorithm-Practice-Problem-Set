'''
If you ask more than 550
 queries during an interaction, your program must terminate immediately, and you will receive the Wrong Answer verdict. Otherwise, you can get an arbitrary verdict because your solution will continue to read from a closed stream.

After printing a query or the answer for a test case, do not forget to output the end of the line and flush the output. Otherwise, you will get the verdict Idleness Limit Exceeded. To do this, use:

fflush(stdout) or cout.flush() in C++;
System.out.flush() in Java;
flush(output) in Pascal;
stdout.flush() in Python;
see the documentation for other languages.
'''

import sys

def print_query_ids(ids):
    length = len(ids)
    # print('?', length, *ids)
    print('?', length, *ids)  # !!! 1-based index
    sys.stdout.flush()  # !!!
    response = int(input())
    return response

def print_query(l, r):
    length = r - l + 1
    # print('?', length, *range(l, r))
    print('?', length, *range(l, r+1))
    sys.stdout.flush()  # !!!
    response = int(input())
    return response

# def print_query_pair(l, r):
#     # print('?', 2, l+1, r+1)
#     print('?', 2, l, r)
#     sys.stdout.flush()  # !!!
#     response = int(input())
#     return response

def find_valid_pair_by_binary(l, r):
    response = print_query(l, r)
    if response == 0:
        return None

    def binary_search(left, right, last_reponse):
        if right - left + 1 == 2:
            return (left, right) 
        
        mid = (left + right) >> 1
        left_response = print_query(left, mid)
        right_response = print_query(mid + 1, right)

        if last_reponse > left_response + right_response:
            i = binary_search(left, mid, left_response) or binary_search(left, mid, last_reponse - right_response) 
            j = binary_search(mid + 1, right, right_response) or binary_search(mid + 1, right, last_reponse - left_response)
            return i if i and print_query(*i) == 1 else j
        else:
            if left_response > 0:
                return binary_search(left, mid, left_response)
            else:
                return binary_search(mid + 1, right, right_response)

    return binary_search(l, r, response)

def find_boarder_by_binary(n):
    lo, hi = 1, n
    while lo < hi:
        mid = (lo + hi) >> 1
        if print_query(lo, mid) > 0:
            hi = mid
        else:
            if print_query(mid, mid+1) == 0:
                lo = mid + 1
            else:
                hi = mid
    return lo

def solve_block(block, left, s):
    length = len(block)
    if length == 0:
        return
    
    response = print_query_ids(block)
    with_left = print_query_ids([left] + block)
    num_right = with_left - response

    if num_right == 0:
        for i in block:
            s[i] = '('
        return
        
    if num_right == length:
        for i in block:
            s[i] = ')'
        return
    
    mid = length // 2
    solve_block(block[:mid], left, s)
    solve_block(block[mid:], left, s)

def interact_io(n):
    s = ['x'] * (n+1)  # 从一开始编号
    # stack = []

    # valid_leftmost_position = -1
    # valid_rightmost_position = -1

    # for i in range(n):
    #     stack.append(i)
    #     while len(stack) >= 2:
    #         l = stack[-2]
    #         r = stack[-1]
    #         response = print_query_pair(l, r)
    #         # response = int(input())
    #         if response == 1:
    #             s[l] = '('
    #             s[r] = ')'
    #             valid_leftmost_position = l
    #             valid_rightmost_position = r
    #             stack.pop()
    #             stack.pop()
    #         else:
    #             break

    # if valid_leftmost_position != -1:


    # print('!', ''.join(s))
    # sys.stdout.flush()  # !!!

    valid_pair_pos = find_valid_pair_by_binary(1, n)

    if valid_pair_pos is None:
        boarder = find_boarder_by_binary(n)
        for i in range(1, n+1):
            if i < boarder:
                s[i] = ')'
            else:
                s[i] = '('
    else:
        l, r = valid_pair_pos
        s[l] = '<'
        s[r] = '>'

        unknown = [i for i in range(1, n+1) if s[i] == 'x']
        DIVIDE = 25
        for block in range(0, len(unknown), DIVIDE):
            solve_block(unknown[block:block+DIVIDE], l, s)

    print('!', ''.join(s[1:]))
    sys.stdout.flush()  # !!!
            







t = int(input())
for _ in range(t):
    n = int(input())
    interact_io(n)


'''
debug:
3
? 3 1 2 3
0
? 2 1 2
0
? 2 2 3
0
! (()
'''