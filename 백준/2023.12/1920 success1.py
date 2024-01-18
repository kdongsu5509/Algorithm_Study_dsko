from bisect import bisect_left

n = int(input())
origin = list(map(int, input().split()))
origin.sort()

m = int(input())
comp = list(map(int, input().split()))

for x in comp:
    result = bisect_left(origin, x)
    print(1 if result != len(origin) and origin[result] == x else 0)
