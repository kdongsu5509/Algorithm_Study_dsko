#백준 1439

def toZeroCnt(num_str):
    #num을 모두 0으로 만드는데 필요한 횟수를 반환
    #num은 0과 1로만 이루어진 문자열
    #num의 길이는 100만 이하
    cnt = 0
    k = 0 
    while k < len(num_str):
        if num_str[k] == '1':
            while num_str[k] == '1':
                k += 1
                if k == len(num_str):
                    k = len(num_str) - 1
                    break
            cnt += 1
        k += 1
    return cnt

def toOneCnt(num_str):
    cnt = 0
    o = 0
    length = len(num_str)
    while o < length:
        if num_str[o] == '0':
            while num_str[o] == '0':
                o += 1
                if o == length:
                    o = length - 1
                    break
            cnt += 1
        o += 1
    return cnt


bin_num = input()
#잠시만, 내가 굳이 정수로 받아야 하나? 문자열로 받아도 되는거 아닌가?

if toZeroCnt(bin_num) < toOneCnt(bin_num):
    print(toZeroCnt(bin_num))
else:
    print(toOneCnt(bin_num))

