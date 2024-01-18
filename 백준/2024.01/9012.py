def is_vps(string):
    #1. 문자열의 길이가 짝수인지 홀수인지 나눈다.
    if(len(string) % 2 != 0):
        # print("len is", len(string))
        return "NO"
    else: #길이가 짝수이면 다른 판별 방식 추가 도입해야함.
        #일차적으로 "(" 와 ")"의 개수가 되야한다.
        if(string.count('(') != string.count(')')):
            return "NO"
        if(string[-1] == '('):
            return "NO"
        
        left_open = 0;
        right_open = 0;
        for x in range(len(string)):
            if string[x] == '(':
                left_open = left_open + 1
            else:
                right_open = right_open + 1

            if left_open < right_open:
                return "NO"
        return "YES"



n = int(input())

for _ in range(n):
    user_in = input()
    print(is_vps(user_in))