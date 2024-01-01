n = int(input())

surface_area = 0
ex_height = 0

height_list = list(map(int, input().split()))

for height in height_list:
    under = 1
    over = 1
    side1 = 4*(height)
    double_side = min(ex_height, height) * 2

    surface_area = surface_area + under + over + side1 - double_side

    ex_height = height

print(surface_area)