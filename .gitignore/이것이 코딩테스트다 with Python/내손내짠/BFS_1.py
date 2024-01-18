from collections import deque

#BFS 메서드 정의
def bfs(graph, start, visited):
    #큐(queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    #현재 노드를 방문 처리
    visited[start] = True

    
    #큐가 빌 때까지 반복

    #참고 : 파이썬에서는 많은 데이터 구조와 자료형에 대해 Boolean 값을 사용할 수 있습니다. 
    #빈 리스트, 빈 문자열, 0, None, 빈 딕셔너리 등과 같이 "거짓"으로 간주되는 값을 가진 데이터 구조나 변수는 
    #False로 간주됩니다
    while queue:
        #큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=" ")
        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

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

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False]*9

#정의된 BFS 함수 호출
bfs(graph, 1, visited)