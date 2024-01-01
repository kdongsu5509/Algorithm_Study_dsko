from collections import deque

def dfs(graph, start, visited):
    visited[start] = True
    print(start+1, end=" ")
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    heap = deque([start])
    visited[start] = True
    while heap:
        pop = heap.popleft()
        print(pop+1, end=" ")
        for i in graph[pop]:
            if not visited[i]:
                heap.append(i)
                visited[i] = True

vertex, edge, start = map(int, input().split())

#입력을 받는 부분
#2차원 배열을 만들어서 인접 행렬 방식 사용

graph = []
for a in range(vertex): 
    t = []
    graph.append(t)
#2차원 배열 완성 2 * vertex

for a in range(edge):
    x, y = map(int, input().split())
    #x,y 로 입력을 받을 거에요. -> x에도 y가 들어가야하고, ,y에도 x가 들어가야한다.
    #x에 y를 넣을거야.
    something1 = graph[x-1]
    something1.append(y-1)
    something2 = graph[y-1]
    something2.append(x-1)

visited1 = [False] * (vertex)
visited2 = [False] * (vertex)

for z in range(vertex):
    s = graph[z]
    s.sort()

dfs(graph, start-1, visited1)
print()
bfs(graph, start-1, visited2)