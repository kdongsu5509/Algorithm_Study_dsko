def prime_check(number):
    is_prime = [True] * (number + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(number**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, number + 1, i):
                is_prime[j] = False

    primes = [num for num in range(2, number + 1) if is_prime[num]]
    prime_factors = []

    for div in primes:
        while number % div == 0:
            prime_factors.append(div)
            number //= div

    return prime_factors

def calculate_lcm_gcd(prime_factors_n, prime_factors_m):
    # 최대 공약수 계산
    gcd = 1
    common_factors = set(prime_factors_n) & set(prime_factors_m)
    for factor in common_factors:
        gcd *= factor

    # 최소 공배수 계산
    part1 = 1
    part2 = 1
    for factor in prime_factors_n + prime_factors_m:
        if factor not in common_factors:
            part1 *= factor
    lcm = part1 * gcd * part2

    return lcm, gcd

m, n = map(int, input().split())

prime_factors_n = prime_check(n)
prime_factors_m = prime_check(m)
lcm, gcd = calculate_lcm_gcd(prime_factors_n, prime_factors_m)

print("최대 공약수:", gcd)
print("최소 공배수:", lcm)
