#8958
score = 0
valsum = 0

n = int(input())
for _ in range(n):
    arr = input()
    for x in arr:
        if x=='O':
            score += 1
            valsum += score
        else: # x=='X'
            score = 0
    print(valsum)
    valsum = 0
    score = 0