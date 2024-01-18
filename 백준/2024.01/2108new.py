n = int(input())  # 최대 500,000(수의 개수)
num_li = [int(input()) for _ in range(n)]  # 최댓값 4000, 최솟값 -4000

# 500,000개라면....
# sort해도 되나?? n*logn -> 500,000 * 20 = 10,000,000 안되겠네.
# 그럼 그냥 4000개의 배열을 만들어서 0~4000까지의 수가 몇개씩 있는지 세자
count_li = [0 for _ in range(8001)]  # -4000~4000까지의 수가 몇개씩 있는지 세는 배열
# 단, 0은 4000번째 인덱스에 저장

total = 0
for num in num_li:
    count_li[num + 4000] += 1
    total += num

# 중앙값 찾기
min_num = 4000
max_num = -4000
cnt = 0

for i in range(8001):
    if count_li[i] != 0:
        # 중앙값 구하기
        cnt += count_li[i]
        if cnt >= n // 2 + 1:
            median = i - 4000
            break

# 최빈값 찾기
mode = None
max_cnt_of_num = max(count_li)
if count_li.count(max_cnt_of_num) == 1:
    mode = count_li.index(max_cnt_of_num) - 4000
else:
    indices = [i - 4000 for i, x in enumerate(count_li) if x == max_cnt_of_num]
    mode = min(indices)

# 범위 계산
range_value = max_num - min_num

# 결과 출력
print(round(total / n))  # 산술평균
print(median)  # 중앙값
print(mode)  # 최빈값
print(range_value)  # 범위
