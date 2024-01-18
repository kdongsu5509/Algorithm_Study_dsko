def solution(s):
    min_length = 1001

    for x in range(len(s)//2):
        cursor = 0
        pressed = ""
        cnt = 0  # 중복되는 횟수.

        if cursor == 0:
            pre = ""
        else:
            pre = s[cursor - x:cursor]
        # 이전 것 처리 완료.

        if pre == s[cursor:cursor+x]:
            while pre == s[cursor:cursor+x]:
                cnt += 1
                cursor = cursor + x
            pressed = str(cnt + 1) + pre
        else:
            pressed = pressed + s[cursor:cursor+x]

        if len(pressed) < min_length:
            min_length = len(pressed)

    return min_length




def solution(s):
    n = len(s)
    min_length = n  # 초기값을 n으로 설정

    for x in range(1, n//2 + 1):  # x는 1부터 n//2까지
        cursor = 0
        compressed = ""
        current_length = 0

        while cursor + x <= n:
            pre = s[cursor:cursor+x]
            cnt = 1

            while cursor + x * cnt + x <= n and pre == s[cursor + x * cnt:cursor + x * (cnt + 1)]:
                cnt += 1

            if cnt > 1:
                compressed += str(cnt) + pre
            else:
                compressed += pre

            cursor += x * cnt
            current_length += len(str(cnt)) + len(pre) if cnt > 1 else len(pre)

        current_length += n - cursor  # 나머지 부분의 길이를 추가

        if current_length < min_length:
            min_length = current_length

    return min_length