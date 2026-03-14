t = int(input())
for _ in range(t):
    n, m, v = map(int, input().split())
    a = list(map(int,input().split()))
    
    prefix = [0]
    acc = 0 
    for v in a:
        acc += v
        prefix.append(acc)
    
    valid = prefix[-1] - (v*m)
    