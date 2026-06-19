num = [2, 7, 11, 15, 23, 21, 91]
target = 36
for i in range(len(num)):
    for j in range(i+1, len(num)):
        for k in range(j+1, len(num)):
            if num[i]+num[j]+num[k]==target:
                print(i, j, k)

