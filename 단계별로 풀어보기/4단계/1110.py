first_num = int(input())
num = first_num
nCycle = 0
while(True):
    plus_num = (num//10) + (num%10)
    num = (num%10)*10 + (plus_num%10)
    nCycle+=1
    if(num == first_num):
        break;
print(nCycle)