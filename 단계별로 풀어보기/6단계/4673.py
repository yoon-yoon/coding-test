#4673
def d(n):
    v_sum = n
    while n!=0:
        v_sum += (n%10)
        n = n//10
    return v_sum

arr = [0 for _ in range(10001)]
n = 1
while True:
    ns = d(n)
    arr[ns]=1
    if arr[10000]==1:
        break
    n+=1
for i in range(1, 9994):
    if arr[i]==0:
        print(i)