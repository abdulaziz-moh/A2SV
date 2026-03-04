n = int(input())
s = list(map(int,input().split()))
s.sort()
maxsum = s[0] + s[1]
left = 0
right = n - 1
ans = 0
while maxsum <= 4:
    while left < right:
        sum = s[left] + s[right]
        if sum > 4:
            right -= 1
        else:
            s[right] += s[left]
            left +=1
            right -=1
    right = n - 1
    ans = right - left + 1
    maxsum = s[left] + s[left + 1]

print (ans)


