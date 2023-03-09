n = int(input())
# print(bin(n)[2:])
answer = ''
def recur(n):
    global answer
    if n == 0:
        return
    else:
        recur(n//2)
        answer += str(n%2)
        return answer
a = recur(n)
print(a)