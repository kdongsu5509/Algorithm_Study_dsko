# DFS 함수 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)



'''
이제부터 이 곳은 분리 공간입니다
왜냐구요?
그냥 그렇다고 하면 시발아 알아서 들어 먹어
이유는 묻지마
짜증나게 하지마
그냥 해!!

BFS is under.'''


from collections import deque

# BFS 함수 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        pop = queue.popleft()
        print(pop, end=" ")
        for i in graph[pop]:  #이차원 배열이니까!
            if visited[i] != True:
                queue.append(i)
                visited[i] = True


def bfs(graph, start, visited):
    heap = deque([start])
    visited[start] = True
    while heap:
        pop = heap.popleft()
        print(pop, end=" ")
        for i in graph[pop]:
            if visited[i] != True:
                heap.append(i)
                visited[i] = True
        

def bfs(graph, start, visited):
    heap = deque([start])
    visited[start] = True
    while heap:
        pop = heap.popleft()
        print(pop, end=" ")
        for i in graph(pop):
            if not visited[i]:
                heap.append(i)
                visited[i] = True

def dfs(graph, v, visited):
    visited[v] = True
    



# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
