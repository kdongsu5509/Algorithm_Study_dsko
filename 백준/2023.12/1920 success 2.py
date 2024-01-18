n = int(input())

origin = list(map(int, input().split()))
origin.sort()
# print(origin)

m = int(input())

comp = list(map(int, input().split()))

def binary_search(li, x):
    low, high = 0, len(li) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = li[mid]

        if mid_value == x:
            return 1
        elif mid_value < x:
            low = mid + 1
        else:
            high = mid - 1

    return 0
        
for x in comp:
    result = binary_search(origin, x)
    print(result)