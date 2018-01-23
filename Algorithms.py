# return fibonachi number
def fib(n):
    if n <= 1:
        return n
    a = [1, 1]
    i = 0
    while i < n:
        a.append(a[i] + a[i + 1])
        i += 1
    return a[i]


# the last digit in fibonachi number
def fib_digit(n):
    if n <= 1:
        return n
    a = [1, 1]
    i = 0
    while i < n:
        a.append((a[i] + a[i + 1]) % 10)
        i += 1
    return a[i]

# input:
# 1 <= n <= 10e18
# 1 <= m <= 10e5
# The goal is to find n mod m
def fib_mod(n, m):
    if n <= 1:
        return n % m
    a = [0, 1]
    i = 0
    while i < n:
        a.append((a[i] + a[i + 1]) % m)
        i += 1
    return a[n] 

# the greatest common divisor
def gcd(a, b):
    return gcd(b, a % b) if b else a



