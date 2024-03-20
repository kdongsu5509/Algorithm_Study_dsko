def solution(board, moves):
    answer = 0 #사라진 인형의 개수
    basket = [0]
    for i in moves:
        pick = board[i - 1][len(board) - 1] #어떤 줄에서 선택받은 인형.
        if(basket[len(basket) - 1] == pick):
            basket.pop()
            basket.insert(0, 0)
            answer += 2
        else:
            basket.append(pick)
    return answer



print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	,[1,5,3,5,1,2,1,4]))