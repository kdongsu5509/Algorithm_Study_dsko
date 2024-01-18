n = int(input()) #1,000,000까지
all_list = list(map(int, input().split()))

m = int(input()) # 100,000까지
buy_list = list(map(int, input().split()))

all_list.sort()
buy_list.sort()

for thing in buy_list:
    start=0
    end = len(all_list)
    mid = len(all_list) // 2
    while(start != end):
        middle = all_list[mid]
        if(middle == thing):
            print("yes")
            break
        else:
            if middle > thing:
                end = mid
                mid = end // 2
            else:
                start= mid
                mid = mid + ((end - mid) // 2)
    print("no")

