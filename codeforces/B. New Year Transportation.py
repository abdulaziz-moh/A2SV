n,t = map(int,input().split())
a = [0] + list(map(int,input().split()))

w_index = 1 + a[1]
while w_index <= t:
    if w_index == t:
        print("Yes")
        break
    
    w_index += a[w_index] 

if w_index != t:
    print("NO")    
    