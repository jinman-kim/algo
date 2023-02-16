n = int(input())
if n == 1:
    print('')
else:
    for i in range(2,n+1):
        while True:
            if n % i == 0 :
                n //= i
                print(i)
            else:
                break
        if n == 1:
            break

