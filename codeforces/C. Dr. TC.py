t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    sum = 0
    for val in s:
        if val == '1':
            sum += n-1
        else:
            sum += 1
    print(sum)