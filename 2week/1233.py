s1, s2, s3 = map(int,input().split())
s1_num = [x for x in range(1,s1+1)]
s2_num = [x for x in range(1,s2+1)]
s3_num = [x for x in range(1,s3+1)]
num = []

for i in range(0,len(s1_num)):
    for j in range(0,len(s2_num)):
        for k in range(0,len(s3_num)):
            sum = s1_num[i] + s2_num[j] + s3_num[k]
            num.append(sum)

print(max(num, key=num.count))
    