# return fibonachi number
def fib(n):
    if n <= 1:
        return n
    a = [0, 1]
    i = 0
    while i < n:
        a.append(a[i] + a[i + 1])
        i += 1
    return a[i]


# the last digit in fibonachi number
def fib_digit(n):
    if n <= 1:
        return n
    a = [0, 1]
    i = 0
    while i < n:
        a.append((a[i] + a[i + 1]) % 10)
        i += 1
    return a[i]
