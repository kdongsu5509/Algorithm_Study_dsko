#백준 18310

n = int(input())

house = list(map(int, input().split()))

house.sort() #170,000

total=sum(house) #100,000

average = total//n

less_than_average = 100000
more_than_average = 0
about_average = []

for i in range(n): #100,000
    if house[i] < average and house[i] < less_than_average:
        less_than_average = house[i]
    elif house[i] > average and house[i] > more_than_average:
        more_than_average = house[i] - average


#compare
total1 = 0
total2 = 0
total3 = 0
for i in range(n):
    total1 += abs(house[i] - less_than_average)
    total2 += abs(house[i] - more_than_average)
    total3 += abs(house[i] - average)

fin_min = min(total1, total2, total3)

if fin_min == total1:
    print(less_than_average)
elif fin_min == total2:
    print(more_than_average)
else:
    print(average)