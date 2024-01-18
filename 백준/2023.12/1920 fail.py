n = int(input())

origin = list(map(int, input().split()))
origin.sort()
# print(origin)

m = int(input())

comp = list(map(int, input().split()))

def div_search(li, x):
    #li = list // x = integer
    middle = li[int(len(li) / 2)]
    print(x, "middle is = ", middle)
    if(middle == x):
        return 1
    elif(middle != x and len(li) == 1):
        return 0
    else:
        first = li[ : int(len(li)/2)]
        second = li[int(len(li)/2) : len(li)]
        if(middle > x):
            return div_search(first, x)
        else:
            return div_search(second, x)
        
for x in comp:
    result = div_search(origin, x)
    print(result)
