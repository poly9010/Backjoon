from collections import deque
import sys

ans = []

for _ in range(int(input())):
    N, doc = map(int, sys.stdin.readline().split())
    printer = deque(map(int,sys.stdin.readline().split()))
    num = deque(range(N))
    num[doc] = "target"
    count = 0
    
    while True:
        output = printer.popleft()
        output_num = num.popleft()
        nothing_big = True
        
        for out in printer: 
            if out > output :
                printer.append(output)
                num.append(output_num)
                nothing_big = False
                break
        if nothing_big:
            count += 1
            if output_num == "target":
                ans.append(count)
                break
                
for x in ans:
    print(x)
        
                
        
        
        
        
                    
            
        
        
                    
        
        
            
            
        
            
                
        
        
            

