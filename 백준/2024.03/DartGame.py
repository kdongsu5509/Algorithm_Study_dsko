def solution(lottos, win_nums):
    # lottos => 내가 산 로또의 번호
    # win_nums = 당첨 번호

    lotto_gewinnen = {}
    # output => 순위.
    answer = []
    cnt = 0
    zeroCnt = 0
    for i in lottos:
        if(i == 0):
            zeroCnt += 1
            # print(zeroCnt)
        elif i in win_nums:
            cnt += 1
            # print("i = ", i, end=" " + ",")
            win_nums.remove(i)
            # print(win_nums)

    answer.append(7 - (cnt + zeroCnt))
    if( 7 - cnt != 7):
        answer.append(7 - (cnt))
    else:
        answer.append(6)
    # 7 - cnt
    return answer

# print(solution([45, 4, 35, 20, 3, 9],	[20, 9, 3, 45, 4, 35])) #{3,5}