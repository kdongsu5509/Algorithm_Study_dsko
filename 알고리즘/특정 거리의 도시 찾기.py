#시발 3연벙해서 그냥 DFS/BFS 일단 제끼고 해야지.

from collections import deque

def bfs(graph, visited, start, distance):
    queue = deque([(start, 0)])  # 큐에 (노드, 거리)의 튜플을 저장하도록 수정
    visited[start] = True
    will_return = []
    
    while queue:
        v, depth = queue.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                queue.append((i, depth + 1))  # 큐에 (노드, 현재 거리 + 1)의 튜플을 저장하도록 수정
                visited[i] = True

        if depth == distance:
            will_return.append(v)

    if not will_return:
        will_return.append(-1)
    return will_return


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m): #1,000,000이라서 시간초과 걸리는 부분같은데....이거 아니면 내가 어떻게 입력받노
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [False] * (n + 1)
return_list = bfs(graph, visited, x, k)

return_list.sort()

for p in return_list:
    print(p)
