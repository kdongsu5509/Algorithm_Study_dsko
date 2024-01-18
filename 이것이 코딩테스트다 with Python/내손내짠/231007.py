#동빈이만 쓰는 큰 수의 법칙
#다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수 만들기

#배열의 특정한 인덱스에 해당하는 수가 연속해서 K번 초과하여 더하기 할 수 없음.
#단, 인덱스가 다르면서 같은 값인 수가 2개 이상인 경우, 이 둘은 다름.

#배열의 크기 N, 숫자가 더해지는 횟수M, K가 제공
#동빈이의 큰 수의 법칙에 따른 결과 출력

n, m, k = map(int, input().split())

numbers = list(map(int, input().split()))
num_li = []

for a in range(n):
    num_li.append(numbers[a])

#max 찾기 - 중복되는 지도 확인
#-> MAX가 중복 -> 걍 M만큼 곱해버려
#-> 중복 아님 -> (max*k)+second max+....

print(numbers)

