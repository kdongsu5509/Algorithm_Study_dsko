n = int(input())

# n의 개수는 20,000까지 감.
# 소문자 단어가 한 줄씩 입력됨
# 길이는 50 이하.

array = []

for _ in range(n):
    user_in = input()
    if array.count(user_in) == 0:
        array.append(user_in)

new_array = sorted(array, key = lambda x : (len(x), x))
print(new_array)




# sorted()


# def qsort(array, start, end):
#     if start >= end:
#         return
#     pivot = start
#     left_num = start + 1
#     right_num = end

#     while left_num <= right_num:
#         while left_num <= end and (len(array[left_num]) < len(array[pivot]) or (len(array[left_num]) == len(array[pivot]) and array[left_num] < array[pivot])):
#             left_num += 1
#         while right_num > start and (len(array[right_num]) > len(array[pivot]) or (len(array[right_num]) == len(array[pivot]) and array[right_num] >= array[pivot])):
#             right_num -= 1

#         if left_num > right_num:
#             array[right_num], array[pivot] = array[pivot], array[right_num]
#         else:
#             array[left_num], array[right_num] = array[right_num], array[left_num]

#     # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
#     qsort(array, start, right_num - 1)
#     qsort(array, right_num + 1, end)

# qsort(array, 0, len(array) - 1)

# for word in array:
#     print(word)
