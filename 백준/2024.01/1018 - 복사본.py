import sys

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

n, m = map(int, input().split())

originalBoard = []

# 입력 부분
for _ in range(n):
    user_in = input().rstrip()
    line = list(user_in)
    originalBoard.append(line)

minimum_cnt = float('inf')  # 무한대로 초기화

# 보드 자르는 부분
for x in range(n - 7):
    for y in range(m - 7):
        # x, y는 스타트 포인트
        sliced_board = []
        for a in range(x, x + 8):
            sliced_line = list(originalBoard[a][y : y + 8])
            sliced_board.append(sliced_line)

        # 시작점이 "W"일 때와 "B"일 때의 경우를 모두 확인
        count_start_w = retouch_cnt(sliced_board, "W")
        count_start_b = retouch_cnt(sliced_board, "B")

        minimum_cnt = min(minimum_cnt, count_start_w, count_start_b)

print(minimum_cnt)


# 첫 번째 코드에서는 슬라이스한 부분에서 첫 번째 색을 기준으로 시작하여 다시 칠해야 하는 정사각형의 개수를 계산합니다. 두 번째 코드에서는 시작점의 색을 "W"와 "B"로 나누어 각각의 경우에 대해 다시 칠해야 하는 정사각형의 개수를 계산하고, 그 중에서 최소값을 찾아냅니다.

# 첫 번째 코드의 경우, 슬라이스한 부분에서 항상 첫 번째 칸의 색을 기준으로 시작하기 때문에 어떤 부분이든 "W"로 시작하게 되면 "W"를 기준으로 다시 칠해야 하는 정사각형의 개수를 계산합니다.

# 두 번째 코드의 경우, 시작점의 색을 구분하여 "W"로 시작할 때와 "B"로 시작할 때 각각의 경우에 대해 다시 칠해야 하는 정사각형의 개수를 계산하고, 그 중에서 최소값을 찾아냅니다. 따라서 각각의 경우에 대한 최소값을 모두 비교하여 가장 작은 값을 선택합니다.

# 예를 들어, 아래와 같은 입력이 주어졌을 때:

# ```
# 9 23
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# ```

# 첫 번째 코드는 항상 "W"로 시작하는 부분을 기준으로 다시 칠해야 하는 정사각형의 개수를 계산하므로 31이 됩니다. 반면에 두 번째 코드는 "W"로 시작하는 경우와 "B"로 시작하는 경우를 모두 고려하여 최소값을 계산하므로 31이 됩니다.

# 결과적으로 두 코드 중 어느 것을 선택할지는 문제의 조건과 목적에 따라 다르게 선택할 수 있습니다.

    # import sys

    # def retouch_cnt(board, start_color):
    #     cnt = 0

    #     for a in range(8):
    #         for b in range(8):
    #             row = a
    #             col = b
    #             current_color = board[row][col]

    #             if (row + col) % 2 == 0 and current_color != start_color:
    #                 cnt += 1
    #             elif (row + col) % 2 == 1 and current_color == start_color:
    #                 cnt += 1

    #     return cnt      
            


    # n, m = map(int, input().split())

    # originalBoard = []

    # #입력 부분
    # for _ in range(n):
    #     user_in = sys.stdin.readline().rstrip()
    #     line = list(user_in)
    #     originalBoard.append(line)

    # #lINE = list(one_line) 과 LINE = list(map(str, one_line.split()))이 왜 차이가 나는거지?
    # #첫 번째는 분할되어서 들어가지고, 두 번째는 분할이 안되네...?
    # #두 번째가 분할이 안되면 시발 왜지? 의도된 거랑 정반대구나...

    # minimum_cnt = 65    
    # #보드 자르는 부분
    # for x in range(n - 7):
    #     for y in range(m - 7):
    #         #x,y는 스타트 포인트
    #         sliced_board = []
    #         for a in range(x, x + 8):
    #             sliced_line = list(originalBoard[a][y : y + 8])
    #             sliced_board.append(sliced_line)

    #         color = sliced_board[0][0]
    #         count = retouch_cnt(sliced_board, color)

    #         if count < minimum_cnt:
    #             minimum_cnt = count
    # print(minimum_cnt)