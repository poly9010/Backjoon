import math

ans = []
while 1:
    s = input()
    if s == '0':
        break
    isPalindrome = True
    if len(s) % 2 == 0: 
        mid = len(s)/2 
    else:
        mid = math.floor(len(s)/2) 

    j = len(s)-1
    for i in range(0,int(mid)):
        if s[i] != s[j]:
            ans.append("no") 
            isPalindrome = False
            break          
        else:
            if j != mid:
                j -= 1
    if isPalindrome:
        ans.append("yes")

for answer in ans:
    print(answer)
    