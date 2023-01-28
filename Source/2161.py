# 2161번 카드1-실버5

from collections import deque

n = int(input())
que = deque(range(1,n+1))
trash = []
first = False
while len(que) > 1:
    
    if not first:
        trash.append(que.popleft())
        first = True
    else:
        que.append(que.popleft())
        first = False
        
print(*trash,que[0]) 
        
    
        