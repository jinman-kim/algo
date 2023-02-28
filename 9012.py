n = int(input())
for i in range(n):
    parenthesis = list(input())
    cnt = 0
    for i in parenthesis:
        if i == '(':
            cnt += 1
        if i == ')':
            cnt -= 1
        if cnt < 0:
            break
    if cnt == 0:
        print('YES')
    else:
        print('NO')