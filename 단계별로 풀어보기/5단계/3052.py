#3052
cont = [0 for i in range(42)]
ans = 0
for _ in range(10):
    num = int(input())
    end = num%42
    cont[end]+=1
for x in cont:
    if(x!=0):
        ans+=1
print(ans)