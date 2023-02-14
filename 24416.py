def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def dp(n):
    f = [0,1]
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    return f[-1],len(f)-3

n = int(input())
a, b = dp(n)
print(a,b)



