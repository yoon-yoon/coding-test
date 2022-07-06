# 2675
t = int(input())
for _ in range(t):
    r, p = input().split()
    r = int(r)
    for i in range(len(p)):
        print(p[i]*r, end="")
    print()