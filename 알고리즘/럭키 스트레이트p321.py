#특정 조건 만족 시 럭키 스트레이트 사용 가능

##특정 조건
#현재 캐릭터 점수 N 이라고 할 때 
#점수 N을 자릿수를 기준으로 반으로 나누어 
#왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을
#더한 값이 동일한 상황을 의미

user_in = input() #n <= 99,999,999

length = len(user_in)

part_1 = user_in[:length//2]
part_2 = user_in[length//2:]

sum_1 = 0
for x in range(len(part_1)):
    sum_1 += int(part_1[x])

sum_2 = 0   
for y in range(len(part_2)):
    sum_2 += int(part_2[y])

if sum_1 == sum_2:
    print("LUCKY")
else:  
    print("READY")
