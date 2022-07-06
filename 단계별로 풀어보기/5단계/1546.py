#1546
ans = 0
ncont = int(input())
n = [int(x) for x in input().split()]
m = max(n)
for i in range(ncont):
    n[i]=n[i]/m*100
    ans+=n[i]
print(ans/ncont)