t = int(input())

for i in range(t):
    a,b = map(int,input().split())

    print(((a//b)*(b-1)) + (a%b))