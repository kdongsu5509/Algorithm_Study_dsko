n, m = map(int, input().split())

sang = []
sun = []

cnt = 0

def binary_search(x, num):
    if len(x) == 1 or x[0] == num:
        return x[0] == num
    elif x[len(x)//2] > num:
        first = x[:len(x)//2]
        return binary_search(first, num)
    else:
        second = x[len(x)//2:]
        return binary_search(second, num)

for _ in range(n):
    num = int(input())
    sang.append(num)

sang.sort()  # 리스트를 정렬해야 이분 탐색이 가능하도록 함

for k in range(m+1):
    if(k == m):
        x, y = map(int, input().split())
    else:
        num = int(input())
        if binary_search(sang, num):
            cnt += 1

print(cnt)
