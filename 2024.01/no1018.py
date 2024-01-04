def retouch_cnt(board, start_color):
    cnt = 0

    for a in range(8):
        for b in range(8):
            row = a
            col = b
            current_color = board[row][col]

            if (row + col) % 2 == 0 and current_color != start_color:
                cnt += 1
            elif (row + col) % 2 == 1 and current_color == start_color:
                cnt += 1

    return cnt

def find_minimum_cnt(board):
    min_cnt = float('inf')

    for start_color in ['W', 'B']:
        for x in range(len(board) - 7):
            for y in range(len(board[0]) - 7):
                sliced_board = [list(board[a][y:y + 8]) for a in range(x, x + 8)]
                count = retouch_cnt(sliced_board, start_color)
                min_cnt = min(min_cnt, count)

    return min_cnt

n, m = map(int, input().split())

original_board = []

# 입력 부분
for _ in range(n):
    user_in = input().rstrip()
    line = list(user_in)
    original_board.append(line)

result = find_minimum_cnt(original_board)
print(result)
