#그 자체로 회문 - 0
# 유사회문 -> 1
# 그 외 -> 2
def check_palindrome(user_In):
    left = 0
    right = len(user_In) - 1
    while(left < right):
        if (user_In[left] != user_In[right]):
            return [2, left, right]
        left += 1
        right -= 1
    return 0
   


many = int(input())

fl = []
for _ in range(many):
    user_In = input()

    re = check_palindrome(user_In)
    if(re == 0):
        fl.append(0)
    else:
        one_more = user_In
        two_more = user_In
        one = re[1]
        two = re[2]
        #case1.
        one_more = one_more[:one] + one_more[one+1:]
        second = check_palindrome(one_more)
        if(second == 0):
            fl.append(1)
        #case2
        else:
            two_more = two_more[:two] + two_more[two+1:]
            second = check_palindrome(two_more)
            if(second == 0):
                fl.append(1)
            else:
                fl.append(2)

for x in fl:
    print(x)
        
    