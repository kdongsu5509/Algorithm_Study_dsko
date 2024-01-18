# n = 배열의 크기 // k = 바꿔치기 연산의 최대 횟수/
n, k = map(int, input().split())
# n 은 최대 십만이다.

list_a = list(map(int,input().split())) # 각 원소는 최대 천만이다.
list_b = list(map(int,input().split()))

#how -> a와 b를 정렬하되 하나는 오름차순, 하나는 내림차순으로 정렬한다. 그리고 비교 후 바꾼다.

sorted_list_a = sorted(list_a)
sorted_list_b = sorted(list_b, reverse=True)

for x in range(k):
    if(sorted_list_a[x] < sorted_list_b[x]):
        sorted_list_a[x], sorted_list_b[x] = sorted_list_b[x], sorted_list_a[x]

sum_of_a = 0
for a in sorted_list_a:
    sum_of_a = sum_of_a + a

print(sorted_list_a)
print(sorted_list_b)

print(sum_of_a)