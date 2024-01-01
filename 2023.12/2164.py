from collections import deque

# 카드의 개수를 입력 받기
n = int(input())

# 1부터 n까지 번호가 매겨진 카드 덱 초기화
카드덱 = deque(range(1, n + 1))

# 하나의 카드만 남을 때까지 카드 회전을 계속 수행
while len(카드덱) > 1:
    # 맨 위의 카드 제거
    제거된_카드 = 카드덱.popleft()
    
    # 다음 카드를 가져와서 맨 아래로 이동
    새로운_카드 = 카드덱.popleft()
    카드덱.append(새로운_카드)

# 마지막으로 남은 카드 출력
print(카드덱[0])