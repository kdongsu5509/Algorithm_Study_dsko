# def prime_factorization(n):
#     factors = []
#     # 2부터 n까지의 소수를 차례대로 확인
#     for i in range(2, int(n**0.5) + 1):
#         while n % i == 0:
#             factors.append(i)
#             n //= i

#     # 남은 수가 소수인 경우
#     if n > 1:
#         factors.append(n)

#     return factors

# def gcd(list_a):
#     mul = 1
#     for x in list_a:
#         mul = mul * x
    
#     return mul

# a, b = map(int, input().split())

# set_a = set(prime_factorization(a))
# set_b = set(prime_factorization(b))
# common = list(set_a.intersection(set_b))

# GCD = gcd(common)
# LCM = (a * b) // GCD

# print(GCD)
# print(LCM) --> fail.


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

# 사용자로부터 두 정수를 입력 받음
a, b = map(int, input().split())

# 최대공약수 계산 및 출력
GCD = gcd(a, b)
print(GCD)

# 최소공배수 계산 및 출력
LCM = lcm(a, b)
print(LCM)
