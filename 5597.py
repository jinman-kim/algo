presence = set([int(input()) for _ in range(28)])
student = set(range(1,31))
result = student - presence
print(min(result))
print(max(result))
