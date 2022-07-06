# 1065
def ret_arr(k):
    arr=[]
    if (k==1000):
        return [1, 0, 0]
    for _ in range(3):
        arr.append(k%10)
        k=k//10
    return arr

cunt = 0
n = int(input())

if (n >= 100):
    for k in range(101, n+1):
        arr = ret_arr(k)
        if (arr[0]-arr[1])==(arr[1]-arr[2]):
            cunt +=1
    cunt+=99
elif (n<100) :
    cunt = n

print(cunt)