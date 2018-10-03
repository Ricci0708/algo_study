# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import itertools
numbers = [int(x) for x in input().split()]
answer = int(input())

result = set()

combinations = itertools.combinations(numbers, 3)
for c in combinations:
    if sum(c) == answer:
        result.add(c)

if not result:
    print("NO")
else:
    result = list(result)
    result.sort()

for r in result:
    print(r[0], r[1], r[2])