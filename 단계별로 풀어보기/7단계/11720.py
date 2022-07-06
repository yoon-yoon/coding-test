# 11720
n = int(input())
num = int(input())
answer = 0
for i in range(n):
    answer += (num % 10)
    num = num // 10
print(answer)