def find_prefix(m):
    stack = [[0,1]]
    prefix = []
    sum = 0
    for v in m:
        temp = [v,1]
        while stack and stack[-1][0] > v:
            temp[1] += stack[-1][1]
            sum -= (stack[-1][0] * stack[-1][1])
            sum += (v * stack[-1][1])
            stack.pop()
        sum += v
        prefix.append(sum)
        stack.append(temp)
    return prefix

rev = m[::-1]
prefix = find_prefix(m)
suffix = find_prefix(rev)[::-1]

mx = [-1,-1]
for i in range(n):
    sum = prefix[i] + suffix[i] - m[i]
    if sum > mx[0]:
        mx = [sum, i]
ans = [0]*n
temp = m[mx[1]]
ans[mx[1]] = temp
for i in range(mx[1]-1,-1,-1):
    if m[i] < temp:
        temp = m[i]   
    ans[i] = temp
    
temp = m[mx[1]]   
for i in range(mx[1]+ 1, n):
    if m[i] < temp:
        temp = m[i]
    ans[i] = temp

print(*ans)