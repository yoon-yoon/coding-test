# 1152
s = [x for x in input().split(" ")]
i = 0
while (i < len(s)):
    if (s[i] ==""):
        s.remove(s[i])
        i-=1
    i+=1
print(len(s))

# 고려사항 : ""이 입력으로 들어왔을 때 s == ["", ""] 이므로 이런 공백 삭제해야 함