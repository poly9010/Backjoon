import sys

N = int(sys.stdin.readline())
text = [""] * N
for i in range(0,N):
    text[i] = input()

output = ""
for i in range(0,len(text[0])):
    ans = text[0][i]
    sum = 0
    for t in text:
        if t[i] == ans:
            sum += 1
    if sum == N:
        output += ans
    else:
        output += '?'
print(output)
    
    
    