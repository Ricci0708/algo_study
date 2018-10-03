# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

li = list(map(int, input().split(' ')))
ans =[]
target = int(input())


for i in range(len(li) - 2):
    ti = li[i]
    if ti >= target:
        continue
    for j in range(i + 1, len(li) - 1):
        tj = ti + li[j]
        if tj >= target:
            break
        for k in range(j + 1, len(li)):
            t = tj + li[k]
            if t == target:
                l = [li[i],li[j],li[k]]
                l.sort()
                if l not in ans:
                    ans.append(l)

if len(ans) != 0:
    for i in range(len(ans)):
        print(str(ans[i][0]) + " " + str(ans[i][1]) + " " + str(ans[i][2]))
else:
    print("NO")