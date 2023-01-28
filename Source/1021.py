# 1021 회전하는 큐 - 실버4

from collections import deque

n, m = map(int, input().split())
que = deque(range(1,n+1))
arr = list(map(int,input().split()))
k = 0
count = 0
while k < m:
    target = arr[k] #현재 뽑아내려는 원소
    if que[0] != target: # 뽑아내려는 위치의 수가 맨 앞에 있지 않다면
        for i in range(0,len(que)):
            if que[i] == target:
                cnt1 = i
                cnt2 = len(que) - i
                if cnt1 < cnt2:
                    for _ in range(cnt1):
                        que.append(que.popleft())
                        count += 1 
                else:
                    for _ in range(cnt2):
                        que.appendleft(que.pop()) 
                        count += 1
    else:
        que.popleft()
        k += 1
        
print(count)
    
