# return fibonachi number
def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    i = 0
    while i < n:
        a, b, i = b, (a + b) % 10, i + 1
    return a


# the last digit in fibonachi number
def fib_digit(n):
    if n <= 1:
        return n
    a, b = 0, 1
    i = 0
    while i < n:
        a, b, i = b, (a + b) % 10, i + 1
    return a

# input:
# 1 <= n <= 10e18
# 1 <= m <= 10e5
# The goal is to find n mod m
def fib_mod(n, m):
    if n <= 1:
        return n % m
    a, b = 0, 1
    i = 0
    while i < n:
        a, b, i = b, (a + b) % m, i + 1
        i += 1
    return a[n] 

# the greatest common divisor
def gcd(a, b):
    return gcd(b, a % b) if b else a

# permutations in the word
def permutations(word):
    pass


# palindrome cheking, if a string is not a palindrome fill it to palindrome
def palindrome_cheking(string):
    i = 0
    string = string.replace(' ', '')
    j = len(string) - 1
    while i < j:
        if string[i] != string[j]:
            return False
        else:
            i += 1
            j -= 1
    return True


# def filling_string_to_palindrome(string):
#     i = len(string)//2 - 1
#     j = len(string)//2 if len(string) % 2 == 0 else len(string)//2 + 1
#     while i > 0 and j < len(string):
#         if string[i] == string[j]:
#             i += 1
#             j -= 1
#         else:
#
#     return i,j


