while True:
    s = input()
    stack = []
    if s == '.':
        break
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        if i == ']':
            if len(stack) and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
        if i == ')':
            if len(stack) and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')