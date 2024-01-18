#4.2
n = int(input())

cnt = 0

time_li = [0,0,0,0,0,0]
check_li = [3,13,23,43,53]
for x in range(30, 40):
    check_li.append(x)

for a in range(n+1):
    for b in range(60):
        for sec in range(60):
            if (a in check_li) or (b in check_li) or (sec in check_li):
                cnt += 1

print(cnt)