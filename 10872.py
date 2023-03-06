def fac(n):
    n = n * (n - 1)
    return n


n = int(input())
answer = n
if n == 0 or n == 1:
    print(1)
else:
    while n > 1:
        n -= 1
        answer *= n

    print(answer)