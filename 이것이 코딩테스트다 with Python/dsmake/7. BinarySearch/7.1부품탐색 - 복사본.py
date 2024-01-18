from bisect import bisect_left

n = int(input()) #1,000,000까지
all_list = list(map(int, input().split()))

m = int(input()) # 100,000까지
buy_list = list(map(int, input().split()))

all_list.sort()
buy_list.sort()

for thing in buy_list:
    p = bisect_left(all_list, thing)
