from collections import deque

def block_check(size, row, col):
    return row < 0 or row >= size or col < 0 or col >= size

n = int(input())  # size
k = int(input())  # number of apples
apples = [list(map(int, input().split())) for _ in range(k)]  # position of the apples
l = int(input())  # 뱀의 방향 변환 횟수
directions = [list(input().split()) for _ in range(l)]  # 뱀의 방향 변환 정보: 초, 방향

# 맵을 만들어서 뱀의 위치를 표시한다. -> 넘어가면 끝난다.
# 0은 빈칸, 1은 뱀의 몸, 2는 사과
board = [[0] * n for _ in range(n)]  # 맵을 만든다.
board[0][0] = 1  # 뱀의 초기 위치를 표시한다.

# 사과 위치
for position in apples:
    board[position[0] - 1][position[1] - 1] = 2

snake_position = deque([[0, 0]])  # 뱀의 위치를 표시한다. 머리가 뒤에, 꼬리가 앞에 위치한다.

sec = 0
snake_head_row = 0
snake_head_col = 0
snake_tail_row = 0
snake_tail_col = 0
movement = 1  # 1: right 2: down 3: left 4: up

while True:
    sec += 1
    if movement == 1:  # right
        snake_head_col += 1
    elif movement == 2:  # down
        snake_head_row += 1
    elif movement == 3:  # left
        snake_head_col -= 1
    elif movement == 4:  # up
        snake_head_row -= 1

    if block_check(n, snake_head_row, snake_head_col) or board[snake_head_row][snake_head_col] == 1:
        print(sec)
        exit()
    else:  # 벽에 부딪히거나, 자기 몸에 부딪히지 않으면
        board[snake_head_row][snake_head_col] = 1  # 일단 길어난 몸 표시.
        snake_position.append([snake_head_row, snake_head_col])

    if board[snake_head_row][snake_head_col] == 2:  # 사과가 있으면 꼬리 그대로.
        snake_position.append([snake_head_row, snake_head_col])
    else:  # 사과가 없으면 꼬리 회수.
        board[snake_tail_row][snake_tail_col] = 0
        snake_position.popleft()
        snake_tail_row, snake_tail_col = snake_position[0]

    if directions and sec == int(directions[0][0]):
        _, turn = directions.pop(0)
        if turn == 'D':
            movement = (movement % 4) + 1
        else:
            movement = (movement - 2) % 4 + 1
