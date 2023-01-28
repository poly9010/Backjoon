# 1406 에디터 - 실버2

import sys


text = list(sys.stdin.readline().rstrip())
arr = []

M = int(sys.stdin.readline())
cursor = len(text)

for _ in range(M):
    order = list(sys.stdin.readline().split())
    
    if order[0] == 'L':
        if text:
            arr.append(text.pop())
    elif order[0] =='D':
        if arr:
            text.append(arr.pop())
    
    elif order[0] == 'B':
        if text:
            text.pop()
    else:
        text.append(order[1])
text.extend(reversed(arr))
print(''.join(text))   

    