# 1157
s = input()
s = s.upper()   # 대문자로
c = []      # 문자열 중복 제거

for value in s:
    if value not in c:
        c.append(value)

res = [] # 인덱스 별 횟수 저장
maxi = 0
same = 0

for i in range(len(c)):
    res.append(s.count(c[i]))
    if(maxi < res[i]):
        maxi = res[i]
    elif(maxi == res[i]):
        same = maxi

if(same == maxi):
    print("?")
else :
    a = res.index(maxi)
    print(c[a])

# 고려사항 : aabbccc와 같이 들어왔을 때 ?가 아닌 c 출력해야 함
# 이를 위해 새롭게 same 변수를 만들어 줌