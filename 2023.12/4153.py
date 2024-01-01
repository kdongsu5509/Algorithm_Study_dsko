def triangle(x,y,z):
    #가장 긴 정수를 찾기.
    side = list()
    side.append(x)
    side.append(y)
    side.append(z)

    side.sort()

    if(pow(side[0], 2) + pow(side[1], 2) == pow(side[2], 2)):
        return "right"
    else:
        return "wrong"

while(True):
    a,b,c = map(int, input().split())
    if(a == 0 and b == 0 and c == 0):
        break

    result = triangle(a,b,c)
    print(result)