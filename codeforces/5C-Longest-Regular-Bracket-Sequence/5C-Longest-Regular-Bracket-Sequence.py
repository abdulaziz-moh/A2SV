s = input()
stack = []
bracket = {'(', ')'}
for v in s:
    if not stack or v == '(':
        stack.append(v)
    else:
        temp = 0
        while stack and stack[-1] not in bracket:
            temp += stack.pop()
        if stack and stack[-1] == '(':
            stack.pop()
            stack.append(temp + 1)
        
        else:
            stack.append(temp)
            stack.append(v)

n = len(stack)
i = 0
arr = []
while i < n:
    
    if stack[i] not in bracket:
        sum = 0
        while i < n and stack[i] not in bracket:
            sum += stack[i]
            i += 1
        arr.append(sum)
    i += 1
    
arr.sort(reverse=True)
length = len(arr)
ans = [0,1]
if length == 1:
    ans[0] = arr[0] * 2
elif length > 1:
    count = 1
    for i in range(1,length):
        if arr[i] == arr[i-1]:
            count += 1
        else:
            break
    ans[0] = arr[0] * 2
    ans[1] = count
print(*ans)