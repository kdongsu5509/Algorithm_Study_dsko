# # test_case_num = int(input())

# # #여기에다가 함수를 전역으로 선언하자
# # def DFS(field, start, cnt):
# #     visited = [[False] * len(field[0]) for _ in range(len(field))]
# #     dx = [-1,0,1,0]
# #     dy = [0,-1,0,1]
# #     y, x = start
# #     visited[y][x] = True
# #     for i in field[y]:
# #         for k in range(4):
# #             ny = y + dy[k]
# #             nx = x + dx[k]
# #             if 0 <= ny <= m and 0<= nx <= n and field[ny][nx] and not visited[ny][nx]:
# #                 DFS(field, (ny, nx), cnt+ 1)
# #     return cnt            



# # for _ in range(test_case_num):
# #     m, n, k = map(int, input().split())
# #     #m은 가로길이, n은 세로길이, ,k는 배우의 위치인데 x,y로 주어진다.
# #     field = [[0]*m for _ in range(n)]
# #     cnt = 1
# #     for _ in range(k):
# #         x,y = map(int, input().split())
# #         field[y][x] = 1

# #     x = DFS(field, (0,0), 1)
# #     print(x)
# test_case_num = int(input())

# def DFS(field, start, cnt):
#     visited = [[False] * len(field[0]) for _ in range(len(field))]
#     dx = [-1, 0, 1, 0]
#     dy = [0, -1, 0, 1]
#     y, x = start
#     visited[y][x] = True
#     for k in range(4):
#         ny = y + dy[k]
#         nx = x + dx[k]
#         if 0 <= ny < len(field) and 0 <= nx < len(field[0]) and field[ny][nx] and not visited[ny][nx]:
#             cnt = DFS(field, [ny, nx], cnt)  # DFS 호출 후 cnt 증가
#     return cnt + 1  # DFS 호출 후에 cnt 증가

# for _ in range(test_case_num):
#     m, n, k = map(int, input().split())
#     field = [[0] * m for _ in range(n)]
#     cnt = 0
#     for _ in range(k):
#         x, y = map(int, input().split())
#         field[y][x] = 1

#     print(DFS(field, [0, 0], 0))  # 초기 cnt는 0으로 전달



#1. DFS : This method cause Recursion Error
def DFS(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return

    if field[y][x] == 1:
        field[y][x] = 0  # 방문한 배추는 0으로 표시
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            DFS(nx, ny)

# 테스트 케이스 개수 입력
test_case_num = int(input())

# 상하좌우 이동을 위한 dx, dy 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(test_case_num):
    # 배추밭의 가로, 세로, 배추의 개수 입력
    M, N, K = map(int, input().split())

    # 배추밭 초기화
    field = [[0] * M for _ in range(N)]

    # 배추 위치 입력
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1

    # 배추 흰지렁이의 개수 초기화
    worm_count = 0

    # 배추밭을 순회하며 DFS 수행
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                DFS(j, i)
                worm_count += 1

    print(worm_count)



#2_DFS
from collections import deque

def DFS(field, start, visited):
    stack = [start]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while stack:
        x, y = stack.pop()
        visited[y][x] = True

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < len(field[0]) and 0 <= ny < len(field) and field[ny][nx] == 1 and not visited[ny][nx]:
                stack.append((nx, ny))
                visited[ny][nx] = True

# 테스트 케이스 개수 입력
test_case_num = int(input())

for _ in range(test_case_num):
    # 배추밭의 가로, 세로, 배추의 개수 입력
    M, N, K = map(int, input().split())

    # 배추밭 초기화
    field = [[0] * M for _ in range(N)]

    # 배추 위치 입력
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1

    # 방문 여부를 나타내는 2차원 배열 초기화
    visited = [[False] * M for _ in range(N)]

    # 배추 흰지렁이의 개수 초기화
    worm_count = 0

    # 배추밭을 순회하며 DFS 수행
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and not visited[i][j]:
                DFS(field, (j, i), visited)
                worm_count += 1

    print(worm_count)


#3 _ Used BFS Algorithm
from collections import deque

# BFS 함수 정의
def BFS(x, y):
    queue = deque([(x, y)])

    while queue:
        cx, cy = queue.popleft()

        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]

            if 0 <= nx < M and 0 <= ny < N and field[ny][nx] == 1:
                field[ny][nx] = 0  # 방문한 배추는 0으로 표시
                queue.append((nx, ny))

# 테스트 케이스 개수 입력
test_case_num = int(input())

# 상하좌우 이동을 위한 dx, dy 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(test_case_num):
    # 배추밭의 가로, 세로, 배추의 개수 입력
    M, N, K = map(int, input().split())

    # 배추밭 초기화
    field = [[0] * M for _ in range(N)]

    # 배추 위치 입력
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1

    # 배추 흰지렁이의 개수 초기화
    worm_count = 0

    # 배추밭을 순회하며 BFS 수행
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                BFS(j, i)
                worm_count += 1

    print(worm_count)
