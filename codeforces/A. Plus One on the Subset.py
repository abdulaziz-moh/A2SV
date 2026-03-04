t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    maximum = max(a)
    minimum = min(a)
    print(maximum - minimum)
