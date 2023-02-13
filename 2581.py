m = int(input())
n = int(input())
def is_prime(num):
    if num == 1:
        return 0
    if num in [2,3]:
        return num
    for i in range(2,num):
        if num % i == 0:
            return 0
    return num


answer = 0
prime = []
for i in range(m,n+1):
    if is_prime(i):
        answer += is_prime(i)
        prime.append(is_prime(i))
if not answer:
    answer = -1
    print(answer)
else:
    print(answer)
    print(prime[0])

