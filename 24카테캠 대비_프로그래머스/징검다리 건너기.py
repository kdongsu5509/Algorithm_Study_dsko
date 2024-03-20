def solution(stones, k):
    left = 1
    right = 200000000
    while left <= right:
        temp = stones.copy()
        mid = (left + right) // 2
        cnt = 0
        for t in temp:
            if t - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1

    return left



'''
def solution(stones, k):

    l = []
    for i, s in enumerate(stones):
        l.append((s, i+1)) 
    l.sort()

    be = [i-1 for i in range(len(stones)+2)]
    ne = [i+1 for i in range(len(stones)+2)]

    answer = 0
    for x in l:
        # value, index
        tv, ti = x

        # 현재 노드가 빠지면서 다음 노드와 이전 노드의 길이를 확인
        if ne[ti] - be[ti] > k:
            answer = tv
            break

        # 이전 노드의 다음 노드는 현재 노드의 다음 노드
        ne[be[ti]] = ne[ti]
        # 다음 노드의 이전 노드는 현재 노드의 이전 노드
        be[ne[ti]] = be[ti]

    return answer
'''