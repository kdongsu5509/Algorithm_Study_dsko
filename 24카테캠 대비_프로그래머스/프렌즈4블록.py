def solution(m, n, board):
    x = [list(row) for row in board]  # board를 복사하여 x에 저장

    answer = 0
    while True:
        # 제거할 블록의 좌표를 저장할 집합
        points = set()

        # 2x2 블록이 있는지 확인하고 좌표를 points에 추가
        for i in range(m - 1):
            for j in range(n - 1):
                if x[i][j] == x[i][j + 1] == x[i + 1][j] == x[i + 1][j + 1] != '팡!':
                    points |= {(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)}

        # 더 이상 제거할 블록이 없으면 반복문 종료
        if not points:
            break

        # 제거된 블록의 개수를 answer에 더함
        answer += len(points)

        # 제거된 블록을 '팡!'으로 표시
        for i, j in points:
            x[i][j] = '팡!'

        # 빈 공간을 채우는 과정
        for j in range(n):
            # 열에서 '팡!'인 블록들을 찾음
            pang_indices = [i for i in range(m) if x[i][j] == '팡!']
            # 해당 열의 '팡!' 블록들을 위에서부터 순회하며 이동시킴
            for k in pang_indices:
                # 블록이 '팡!'인 동안 위로 이동시킴
                while k > 0 and x[k][j] == '팡!':
                    x[k][j], x[k - 1][j] = x[k - 1][j], x[k][j]
                    k -= 1

    return answer


print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
