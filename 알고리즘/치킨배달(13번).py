#백준 15686

def Combination(chicken, m):
    re = []
    for i in range(len(chicken)):
        if m == 1:
            re.append([chicken[i]])
        else:
            for next in Combination(chicken[i+1:], m-1):
                re.append([chicken[i]] + next)
    return re

def city_chicken_distance(selected_chicken, house):
    city_distance = 0
    for i in range(len(house)): #집 별로 치킨 거리를 구합니다.
        temp = house_chicken_distance(selected_chicken, house[i])
        city_distance += temp
    return city_distance

def house_chicken_distance(selected_chicken, selected_house):
    #selected_chicken은 리스트입니다. -> 반복 대상이에요.
    #selected_house는 한 개의 집입니다. -> 노 반복.(기준점)
    distance = 100
    for fix_chicken in selected_chicken:
        temp = abs(fix_chicken[0] - selected_house[0]) + abs(fix_chicken[1] - selected_house[1])
        if temp < distance:
            distance = temp
    return distance

#1. 입력 받기
n, m = map(int, input().split())

city = []

for a in range(n):
    data = list(map(int, input().split()))
    city.append(data)


#2. 치킨집과 집의 위치 찾기
chicken = []
house = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append([i,j])
        elif city[i][j] == 1:
            house.append([i,j])

#3. 치킨집 중 m개를 뽑는 조합 구하기
chicken_c = Combination(chicken, m)


min_city_distance = 100000000000000
for chicken_list in chicken_c:
    temp = city_chicken_distance(chicken_list, house)
    if temp < min_city_distance:
        min_city_distance = temp

print(min_city_distance)