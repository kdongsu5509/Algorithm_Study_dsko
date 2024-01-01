from collections import deque

n, m = map(int, input().split())

maze = []
for i in range(n):
    maze.append(list(map(int, input())))

def bfs(maze, start, end):
    dx = [-1, 1, 0, 0]  # 상하좌우 이동을 나타내는 리스트
    dy = [0, 0, -1, 1]

    queue = deque([start + (1,)])  # 시작 지점과 이동한 칸 수를 큐에 추가
    visited = [[False] * m for _ in range(n)]  # 방문 여부를 저장하는 배열

    while queue:
        x, y, count = queue.popleft()

        if (x, y) == end:
            return count  # 목적지에 도착하면 이동한 칸 수 반환

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny, count + 1))
                visited[nx][ny] = True

    return -1  # 도착할 수 없는 경우 -1 반환
start = (0, 0)
end = (n-1, m-1)

# BFS 호출 및 결과 출력
result = bfs(maze, start, end)
print(result)