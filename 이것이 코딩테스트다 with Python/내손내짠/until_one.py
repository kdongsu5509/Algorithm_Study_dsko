n, k = map(int,input().split())

cnt = 0

while(n>1):
    if(n%k == 0):
        n = n/k
    else:
        n -= 1
    cnt += 1

print(cnt)

# n, k = map(int,input().split())
# result = 0

# while n>= k:
#     while n%k != 0:
#         n -= 1
#         result += 1
#     n//=k
#     result += 1

# while n>1:
#     n -= 1
#     result += 1

# print(result)


n, k = map(int,input().split())
result = 0

while True:
    target = (n//k)*k
    result += (n-target) #1개씩 뺀 것을 1개씩 값을 더하지 않음.
                        #뭉터기로
    n =target
    if n<k:
        break
    result += 1 #어차피 위 구문에서 break가 되지 않는다면? 이 문장이랑 밑에 문장 둘 다 수행
    n//=k #계산 전에 계산 횟수를 먼저 추가한 거임.

#마지막으로 남은 수(break되서 계산 못된 n)에 대하여 1씩 빼기
result += (n-1)
print(result)