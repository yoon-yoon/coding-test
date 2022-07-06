#2577
abc = 1
cont = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 세 수를 입력받아 곱
for i in range(3):
    data = int(input())
    abc= abc * data
while(True):
    end = abc%10
    abc = abc//10
    cont[end]+=1
    if(abc == 0):
        break
for x in cont:
    print(x)