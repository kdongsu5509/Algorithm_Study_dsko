def find_index(list,name, length):
    position = length
    mid = position // 2
    while(True):
        if(position >= 2):
            if(list[mid] == name):
                return ((mid) + 1)
            else:
                if(name < list[mid]):
                    position = mid
                else:
                    list = list[mid : position]
                    position = mid
        else:
            if(list[mid] == name):
                return mid + 1
            else:
                return -1


n, m = map(int, input().split())
#m = 100,000 그렇다면 두 수를 비교해야 하는데,,,, 이미 n + m = max 200,000이다.

poketmon_list = []

for _ in range(n):
    name_of_poketmon = input()
    poketmon_list.append(name_of_poketmon)

sorted_poketmon_list = sorted(poketmon_list)

for _ in range(m):
    problem = input()
    #입력은 문자로 들어올 수도, 숫자로 들어올 수도 있다.
    #try, except구문 사용하자

    try:
        changed_problem = int(problem)
        #숫자로 문자를 반환하는 함수
        print("==",poketmon_list[changed_problem - 1])
    except:
        changed_problem = problem
        #문자로 숫자를 반환하는 함수
        print("==",find_index(sorted_poketmon_list,changed_problem, n))

