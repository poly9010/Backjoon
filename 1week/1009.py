import sys
sys.setrecursionlimit(1000000)

T = int(sys.stdin.readline())
ans = [0]*T
for i in range(0,T):
    a, b = map(int, sys.stdin.readline().split())
    num = a % 10
    if num == 0:
        ans[i] = 10
    elif num in [1,5,6]:
        ans[i] = num
    elif num in [4,9]:
        if b % 2 == 0:
            ans[i] = num ** 2 % 10
        else:
            ans[i] = num
    else:
        if b % 4 == 0:
            ans[i] = num ** 4 % 10
        else:
            ans[i] = num ** (b % 4) % 10
for answer in ans:
    print(answer) 
    
    
    
