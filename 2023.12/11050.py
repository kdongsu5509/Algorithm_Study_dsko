# import math

# def factorial(n, dfualt = 1):
# 	return math.factorial(n-k) // math.factorial(k)

n, k = map(int, input().split())

def factorial(n):
    head = 1
    for x in range(2, n+1):
        head = head * x
    return head

head = factorial(n)
# print(head)
body = (factorial(n-k)) * (factorial(k))
# print(body)

re = head / body

print(int(re))