n = int(input())
x, y = 1,1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0 ,0]
move_types=["L", 'R', "U", "D"]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx>n or ny >n:
        continue
    x, y = nx, ny

print(x, y)


# 주어진 코드에서 x와 y가 1보다 작아지지 않고 n보다 커지지 않는 이유는
#  if nx < 1 or ny < 1 or nx > n or ny > n:라는 조건문 때문입니다. 
# 이 조건문은 다음과 같이 작동합니다:

# nx < 1은 x 좌표가 1보다 작을 때 True가 됩니다.
# ny < 1은 y 좌표가 1보다 작을 때 True가 됩니다.
# nx > n은 x 좌표가 n보다 클 때 True가 됩니다.
# ny > n은 y 좌표가 n보다 클 때 True가 됩니다.

# 만약 이 중 어느 하나의 조건이 True가 되면, 
# continue 문이 실행되어 현재의 반복(iteration)을 중지하고 다음 반복으로 넘어갑니다. 

# 따라서 x와 y가 1보다 작아지거나 n보다 커지는 경우에는 
# 이 조건문을 통과하지 못하고 반복문이 다음 단계로 진행하지 않습니다.

# 즉, 코드는 현재 위치에서 이동 계획(plans)에 따라 새로운 좌표(nx, ny)를 계산하고, 
# 그 좌표가 범위를 벗어나지 않을 때만 x와 y를 업데이트합니다. 
# 범위를 벗어나는 경우에는 아무런 업데이트 없이 현재 위치를 유지하게 되므로 
# x와 y가 1보다 작아지거나 n보다 커지지 않는 것입니다.

# continue 문은 현재의 반복(iteration)을 중지하고 다음 반복으로 넘어가게끔 만듭니다. 
# 따라서 continue 문이 실행되면 해당 반복문 내에서 continue 아래에 있는 코드들은 실행되지 않고, 
# 다음 반복(iteration)으로 넘어갑니다.