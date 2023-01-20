c1 = input()
c2 = input()
c3 = input()

color = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
for i in range(0,len(color)):
    num = ""
    if c1 == color[i]:
        num += str(i)
        for j in range(0,len(color)):
            if c2 == color[j]:
                num += str(j)
                
print(num)
for i in range(0,len(color)):
    if c3 == color[i]:
        num = int(num) * pow(10,i)
print(num)