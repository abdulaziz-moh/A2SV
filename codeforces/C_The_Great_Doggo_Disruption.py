
from typing import Counter

n = int(input())
a = input()
arr = []
for v in a:
    arr.append(v)
if len(arr) <= 1:
    print("Yes")
else:
    arr.sort()
    count = Counter(arr)

    for v in count.values():
        if v > 1:
            print("Yes")
            break
    else:
        print("No")