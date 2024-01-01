def sieve_of_eratosthenes(m, n):
    # 초기화: 2부터 n까지의 모든 수를 포함하는 리스트 생성
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

    # 에라토스테네스의 체 알고리즘 수행
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # i의 배수들을 모두 제거
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    # 소수만 남긴 리스트 생성
    primes = [num for num in range(m, n + 1) if is_prime[num]]
    return primes

m, n = map(int, input().split())

# 예시: 1부터 30까지의 소수를 찾아서 출력
result = sieve_of_eratosthenes(m,n)

for k in result:
    print(k)

