time = int(input())

fl = []
for _ in range(time):
    total = 0
    user_In = int(input())
    #1로만 이루어진 수 => user_In
    total += 1

    twoIs = 0
    threeIs = 0
    #일단, 2로만 이루어진 수의 개수를 구하자.
    #2로 나누어 떨어지면, 2로만 이루어진 수이다.
    if (user_In % 2 == 0):
        total += 1
        twoIs = user_In // 2
    else:
        twoIs = user_In // 2
    ########################################3
    if (user_In%3 == 0):
        total += 1
        threeIs = user_In // 3
    else:
        threeIs = user_In // 3
    
    #1,2f로만 이루어진 수
    for x in range(1, twoIs+1):
        if (user_In - 2 * x > 0):
            total += 1
    
    #1,3으로만 이루어진 수
    for x in range(1, threeIs+1):
        if (user_In - 3 * x > 0):
            total += 1

    #2,3으로만 이루어진 수 
    for x in range(1, twoIs+1):
        for y in range(1, threeIs+1):
            if (user_In - 2 * x - 3 * y == 0):
                total += 1
            
    #1,2,3으로만 이루어진 수
    for x in range(1, twoIs+1):
        for y in range(1, threeIs+1):
            if (user_In - 2 * x - 3 * y > 0):
                total += 1
    fl.append(total)
for x in fl:
    print(x)



# T = int(input())

# for t in range(T):
#     n = int(input())
#     count = 0
#     while n >= 0:
#         # print(count)
#         count += 1
#         count += n // 2
#         n = n - 3

#     print(count)