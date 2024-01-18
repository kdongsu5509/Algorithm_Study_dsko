n, m = map(int, input().split())
# n=볼링공의 개수(1~1000), m=볼링공의 최대 무게(1~10)

weight = list(map(int, input().split()))

#서로 다른 무게의 공을 고르는 경우의 수를 구하라.
## 무게가 같아도 서로 다른 공이다.

cnt = 0 

for i in range(n):
    for j in range(i+1, n):
        if weight[i] != weight[j]:
            cnt += 1

print(cnt)