#10818
n = int(input())
lst = [int(x) for x in input().split()]
mini = lst[0]
maxi = lst[0]
for i in range(1, n):
    if(mini > lst[i]):
        mini = lst[i]
    if(maxi < lst[i]):
        maxi = lst[i]
print(mini, maxi)