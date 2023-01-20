n, m = map(int,input().split())
status = [input() for _ in range(n)]
r, c = 0, 0
    
for i in range(0,n):
    if 'X' not in status[i]:
        r += 1

for i in range(0,m):
    list = [status[j][i] for j in range(0,n)]
    if 'X' not in list:
        c += 1
print(max(r,c))