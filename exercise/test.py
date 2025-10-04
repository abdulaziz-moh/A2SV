from collections import Counter
hm = Counter()
hm['x'] += 2
hm['a'] = 0
hm['b'] = 1
print(max(hm.values()))
