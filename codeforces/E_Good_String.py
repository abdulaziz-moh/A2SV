n = int(input())
s = input()

ans = []
for v in s:
    if len(ans)%2 == 0:
        ans.append(v)
    elif v != ans[-1]:
        ans.append(v)
if len(ans) %2 != 0:
    ans.pop()
print(n - len(ans))
print("".join(ans))