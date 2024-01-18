# 숫자카드게임 ; 여러 개의 숫자 카드 중 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임.

# rule
# 숫자가 쓰인 카드->n*m 형태로 배치되어 있음
# 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택
# 그 후 선택된 행에 포함된 카드들 중에서 가장 숫자가 낮은 카드를 뽑아야 함
# 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 가장 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 카드를 뽑을 수 있도록 전략을 세워라.

n,m = map(int, input().split())
#굳이 n*m 사이즈 2차원 배열을 우선 선언하여 메모리를 할당 후에 숫자를 넣을 필요 없음

choosed_list = []
for a in range(n):
    s_list = list(map(int, input().split()))
    min_num = min(s_list)
    choosed_list.append(min_num)
    #혹은
    #for문 선언 전 result = 0 선언
    #choosed_list에 삽입 후 max 써도 되지만
    #result = max(result, min_num)이라는 코드를 사용하여 출력할 값을 result라는 공간에 할당한 후
    #result를 출력

print(max(choosed_list))
