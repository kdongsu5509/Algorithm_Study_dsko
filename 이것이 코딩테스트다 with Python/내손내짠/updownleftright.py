#공간의 크기 입력받기
n = int(input())
plan = list(map(str, input().split()))

#n*n공간이 생성됨.
#초기 위치를 일차원 배열로 나타낼 예정
now = [1, 1]

#조건문으로 반복하자
for a in range(len(plan)):
    if plan[a] == "U":
        now[0] -= 1
        if now[0] == 0:
            now[0] += 1
    elif plan[a] == "D":
        now[0] += 1
    elif plan[a] == "R":
        now[1] += 1
        if now[1] > n:
            now[1] = n
    elif plan[a] == "L":
        now[1] -= 1
        if now[1] == 0:
            now[1] += 1

print(now[0], now[1])