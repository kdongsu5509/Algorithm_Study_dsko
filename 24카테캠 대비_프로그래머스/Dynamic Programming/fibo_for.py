#한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화

d = [0] * 100

# 피보나치 함수를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)

d[1] = 1
d[2] = 1
n = 99

#보텀업 다이나믹 프로그래밍
for i in range(3, n+1):
    d[i] = d[i - 1] +d[i-2]

print(d[n])


###메모이제이션은 탑다운 방식에 국한되어 사용되는 표현