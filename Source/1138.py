import sys

n = int(sys.stdin.readline())
info = list(map(int,input().split()))# 자신보다 키가 큰 사람이 몇명이나 왼쪽에 있는지에 대한 정보
order = [-1 for _ in range(n)] # 줄을 세우기 위한 리스트

for i in range(0,n): #i는 현재 줄을 매겨야할 사람
    #키가 가장 작은 사람의 왼쪽에 있는 사람의 수가 그 사람의 줄 번호
    count = info[i] 
    k = 0
    while k < n:
        if order[k] == -1 and count > 0:
            count -= 1
        elif order[k] == -1 and count == 0 :
            order[k] = i+1 
            print(order)
            break
        k += 1   
print(*order)
    
        
