n = int(input())

board = {}
round = []

winner = None
max_score = -1000*1000 - 10


for i in range(n):
    name, score = input().split()
    score = int(score)
    round.append((name, score))

    if name not in board:
        board[name] = score
    else:
        board[name] += score

    # if board[name] > max_score:
    #     max_score = board[name]
        # winner = name

for name, score in board.items():
    if score > max_score:
        max_score = score
        # winner = name

# print(max_score)

board_rerun = {}
for name, score in round:
    # print(name, score)
    if name not in board_rerun:
        board_rerun[name] = score
    else:
        board_rerun[name] += score
    
    # print(name, board[name], board_rerun[name], max_score)

    # if board[name] == max_score:
    if board[name] == max_score and board_rerun[name] >= max_score:
        winner = name
        print(winner)
        exit()
