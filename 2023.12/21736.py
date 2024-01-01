n , m = map(int, input(). split())

campus = [] #2차원 배열

x = 0
y = 0

for column in range(n):
    input_row = input()
    campus.append(input_row)
    for row in range(m):
        if(input_row[row] == 'I'):
            x = row
            y = column


movement = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def DFS(list):
    Check = [False] * len(list)

    

print(x, y)
