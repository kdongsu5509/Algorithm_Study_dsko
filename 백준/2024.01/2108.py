## 산술평균 -> n개의 수들들의 합  // n
## 중앙값 -> n개의 수들을 증가하는 순서로 나열했을 때 그 중앙에 위치하는 값
## 최빈값 -> n개의 수들 중 가장 많이 나타나는 값
## 범위 -> n개의 수들 중 최댓값과 최솟값의 차이

n = int(input()) #최대 500,000(수의 개수)

num_li = [int(input()) for _ in range(n)] #최댓값 4000, 최솟값 -4000

#500,000개라....
## sort해도 되나?? n*logn -> 500,000 * 20 = 10,000,000 안되겠네.
## 그럼 그냥 4000개의 배열을 만들어서 0~4000까지의 수가 몇개씩 있는지 세자 

count_li = [0 for _ in range(8001)] #-4000~4000까지의 수가 몇개씩 있는지 세는 배열
#단, 0은 4000번째 인덱스에 저장

total = 0
for num in num_li:
    count_li[num+4000] += 1
    total += num

print("_________________________")

#산술평균
print(round(total/n)) ##이상없음.
#중앙값/최빈값/범위  -> 최빈값이 완전탐색에서 좀 걸리네.

#일단 중앙값 찾아야징
# min_num = float('inf')  # 무한대로 초기화
min_num = num_li[0] 
max_num = -4001
max_cnt_of_num = 0
cnt = 0
for i in range(8001):
    if count_li[i] != 0: #그 값이 존재한다. -> as index
        if (i - 4000) > max_num:
            max_num = (i - 4000)
        elif (i - 4000) < min_num:
            min_num = (i - 4000)
        
        #최빈값 구하는 알고리즘
        if count_li[i] > max_cnt_of_num:
            max_cnt_of_num = count_li[i]

        #중앙값 구하는 코드
        if cnt < n//2 + 1:
            cnt += count_li[i]

print(max_num)
print(min_num)

print(cnt - 1) ##error1
print(max_cnt_of_num) ##error2
print(4000 - abs(max_num - min_num)) #이것도 완전 탐색인데. -> 완전 탐색에서 max_num, min_num을 구했으니까 이걸로 해결 가능
