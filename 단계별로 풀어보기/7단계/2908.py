# 2908
a, b = input().split()
a = int(a)
b = int(b)
aa = ""
bb = ""
for _ in range(3):
    aa += str(a%10)
    a = a//10
    bb += str(b%10)
    b = b//10

if (int(aa) > int(bb)):
    print(aa)
else:
    print(bb)