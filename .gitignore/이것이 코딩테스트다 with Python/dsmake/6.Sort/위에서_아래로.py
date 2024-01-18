n = int(input())

numbers = []

#입력을 받아 리스트에 저장합니다.
for a in range(n):
    user_in = int(input())
    numbers.append(user_in)

numbers.sort()
numbers.reverse()

for x in range(n):
    print(numbers[x], end=" ")