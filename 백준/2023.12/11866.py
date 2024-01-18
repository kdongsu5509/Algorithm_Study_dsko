n, k = map(int, input().split())

def circle_pop(li, k):
    position = 0
    result = []  # 결과를 저장할 리스트 추가
    while len(li) > 0:
        position = (position + k - 1) % len(li)
        popped = li.pop(position)
        result.append(popped)  # 결과 리스트에 추가
    return result

numbers = list(range(1, n + 1))

result_list = circle_pop(numbers, k)
result_str = '<' + ', '.join(map(str, result_list)) + '>'
print(result_str)
