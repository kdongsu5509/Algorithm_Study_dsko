#맵 사이즈 : 세로 크기 sero / 가로 크기 garo
sero, garo = map(int, input().split())

#현 위치 좌표 2개, 방향 1개
a,b,d = map(int, input().split())

#육지, 바다 정보 / nㅇ개의 줄에 북에서 남으로 / 각 줄에서는 서에서 동으로
#0 -> 육지 / 1 ->바다

all_map = []
for x in range(sero):
    mini_garo = list(map(int, input().split()))
    all_map.append(mini_garo)

move = [[-1, 0, 0],[]]
