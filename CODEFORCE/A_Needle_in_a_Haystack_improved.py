from collections import defaultdict


t = int(input())
for _ in range(t):
    s = input()
    t = input()

    count = defaultdict(int)
    for v in t:
        count[v] += 1
        
    for v in s:
        if count[v] == 0:
            print("Impossible")
            break
        count[v] -= 1   
    else:
        alphabet =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        ans = []
        for v in s:
            i = 0
            while alphabet[i] < v:
                for _ in range(count[alphabet[i]]):
                    ans.append(alphabet[i])
                    count[alphabet[i]] -= 1
                i += 1
            ans.append(v)
        for ch in alphabet:
            for _ in range(count[ch]):
                ans.append(ch)
        print("".join(ans))