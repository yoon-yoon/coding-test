#4344
c = int(input())
for _ in range(c):
    arr = [int(x) for x in input().split()]
    vsum = sum(arr[1:])
    n = arr[0]
    avrg = vsum/n
    people = 0

    for i in range(1, n+1):
        if(arr[i]>avrg):
            people+=1
    print(f"{round((people/n)*100, 3):.3f}%")