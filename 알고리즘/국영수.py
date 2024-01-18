#백준 10825

n = int(input())

all_grade = []

for _ in range(n):
    name, ko, en, math = map(str, input().split())
    personal_grade = [name, int(ko), int(en), int(math)]
    all_grade.append(personal_grade)
#n은 100,000이다.
    
#각 정렬 별로 시간 복잡도를 계산해서 무엇을 사용할 지 정하자.
#파이선 내장 함수 -> 100,000 * 17 = 1,700,000 -> 1초 안에 가능
    
all_grade.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for _ in all_grade:
    print(_[0])