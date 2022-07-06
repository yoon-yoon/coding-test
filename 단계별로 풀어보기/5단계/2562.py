#2562
data = []
maxi = 0
idx = 0
for i in range(9):
    data.append(int(input()))
    if(maxi < data[i]):
        maxi = data[i]
        idx = i
print(f"{maxi}\n{idx+1}")