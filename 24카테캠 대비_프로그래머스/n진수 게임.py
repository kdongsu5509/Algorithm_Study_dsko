def solution(n, t, m, p):
    # n = 진법
    # t = 미리 구할 숫자의 갯수
    # m = 게임에 참가하는 인원
    # p = '튜브'의 순서
    final_str = "0"
    now_num = 1
    total_length = t * m
    if (len(final_str) < total_length):
        while (len(final_str) <= total_length):
            final_str += toNnum(now_num, n)
            print("final_str =======> ", final_str)
            now_num += 1

    answer = ''
    idx = p - 1
    while (len(answer) < t):
        answer += final_str[idx]
        idx += m

    return answer


def toNnum(original, N):
    # original을 n진법으로 변환한 str를 반환.
    return_str = ""
    toAlph = {10 : "A", 11 : "B", 12 : "C", 13 : "D", 15:"E", 16:"F"}
    while (original > 0):
        temp = original % N
        if temp < 10:
            return_str = str(temp) + return_str
        else:
            tempStr = str(toAlph.get(temp))
            return_str = tempStr + return_str
        original //= N
    return return_str

print(solution(16,	16,	2,	1)) #0111"