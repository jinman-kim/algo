import sys
from collections import deque
queue = deque()
for _ in range(int(input())):
    command = sys.stdin.readline()
    if 'push' in command:
        queue.append(int(command.split()[1]))
    if 'front' in command:
        if queue:
            print(queue[0])
        else:
            print(-1)
    if 'back' in command:
        if queue:
            print(queue[-1])
        else:
            print(-1)
    if 'empty' in command:
        if not queue:
            print(1)
        else:
            print(0)
    if 'size' in command:
        print(len(queue))
    if 'pop' in command:
        if queue:
            tmp = queue.popleft()
            print(tmp)
        else:
            print(-1)