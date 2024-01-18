import math

n = int(input())

user_info = []

for cnt in range(n):
    age, name = input().split()
    age = int(age)
    Tuple = (age, cnt, name)
    user_info.append(Tuple)

sorted_info = sorted(user_info)    


for user in sorted_info:
    print(user[0], user[2])

#백 이십만 정도? 1초 안에 쌉가능 할 듯.