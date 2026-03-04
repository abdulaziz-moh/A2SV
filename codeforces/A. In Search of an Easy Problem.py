n = int(input())
ans = list(map(int,input().split()))
for v in ans:
    if v == 1:
        print("HARD")
        break
else:
    print("EASY")