

def isPrime(x):
    for i in range(2,int(x/2)+1):
        if x % i == 0:
            return False
    return True
        
def k(x):
    count = 0
    for i in range(2,int(x/2)+1):
        while x % i == 0:
            if isPrime(i):
                count += 1
            x = x/i
    return count
            
a, b = map(int, input().split())
cnt = 0
prime = [i for i in range(a,b+1)] 

for i in range(0,len(prime)):
    if prime[i] != 0 and isPrime(prime[i]):
        for j in range(i+prime[i],len(prime),prime[i]):
            prime[j] = 0 ##소수만 냅두고 0으로바꿈
print(prime)
    
for i in range(a,b+1):
    if i not in prime:
        num = k(i)
        if isPrime(num):
            cnt += 1
print(cnt)
    
    
    