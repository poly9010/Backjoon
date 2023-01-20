from itertools import combinations
n, m, k = map(int, input().split())
outcomes = [*combinations([i for i in range(n)], m)]
print(outcomes[2])
cnt = 0
# for num in outcomes:
#     if num
    

