n, m, k = map(int, input().split())

numbers = list(map(int, input().split()))

big = max(numbers)
sec = 0
for a in numbers:
    if a<big and sec<a:
        sec = a

total = 0
cnt = 0 
while(m>0):
    while(cnt<k):
        total = total + big
        cnt+=1
        m -= 1
    cnt = 0
    total+=sec
    m -= 1
#위 코드는 가장 큰 수와 두 번째로 큰 수를 구하는 코드이다. ->그러나 오류 발생 가능성 있음
#바로, 가장 큰 수가 2개 이상일 때.
#해결방법
#numbers.sort() 한 후에 인덱스를 이용(numbers[n-1], numbers[n-2])


print(total)


# ______________입력받는 수의 개수가 매우 커질 경우______________________
# 반복에서 규칙 찾기
# 수열이 반복되는 횟수 => m/(k+1)
# 가장 큰 수가 등장하는 횟수 => 수열이 반복되는 횟수 * 반복하여 사용할 수 있는 횟수
# **m이 k+1로 나누어 떨어지지 않는 경우 -> M % (k+1)만큼 큰 수가 추가로 더해짐.
# 위의 규칙을 이용하면 큰 수의 입력이라도 빠른 시간내에 처리 쌉가능.
