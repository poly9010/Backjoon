import sys

n = int(input())
sys.setrecursionlimit(10 ** 6)

leaders = [0 for _ in range(n)]
same = [[0 for _ in range(n)] for _ in range(n)]
info = []

for i in range(n):
     info.append(input().split())
     
for i in range(0,n): # 기준학생
    for j in range(0,5): # 학년
        for k in range(0,n): # 다른학생 
            if info[i][j] == info[k][j]:
                if same[i][k] == 0 :
                    same[i][k] += 1
                    
list = []
for i in range(0,len(same)):
       list.append(same[i].count(1))
print(list.index(max(list))+1)
    
