n, m = map(int, input().split())


frame = [[0] * m for _ in range(n)]

for i in range(n):
    frame[i] = list(input())
#입력 완료
    
visited = [[False] * m for _ in range(n)]

print(visited)