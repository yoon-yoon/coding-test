n, x = input().split()
lst = [int(x) for x in input().split()]
answer = []
for i in range(int(n)):
    if lst[i] < int(x):
        answer.append(lst[i])
for num in answer:
    print(num, end=" ")