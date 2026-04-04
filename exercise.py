# from typing import Counter


# t = int(input())
# for _ in range(t):
#     a = input()
#     count = Counter(a)
#     if count['0'] == 0 or count['1'] == 0:
#         print(0) 
    
#     elif count['0'] == count['1']:
#         print(count['0']-1)
      
#     else:
#         print(min(count['0'], count['1']))
    
#    gh 
# t = int(input())
# for _ in range(t):
#     d,t = map(int,input().split())
#     x = 1
#     c = 0
#     while d > t * x:
#         x *= 2
#         c += 1
#     print(c)
# from collections import Counter
# t = int(input())

t = int(input())
for _ in range(t):
    s = input().strip()
    c =0
    i =0 
    n = len(s)
    while i < n:
        j = i+1
        while j<n and s[j]!= s[i]:
            j+=1
        if j<n:
            c+=2
            i=j+1
        else:
            break
    
    print(n-c)



# t = int(input())
# for _ in range(t):
#     n = int(input())
#     s = input()
    
#     mid = n//2
#     ch, count = s[mid], 0
    
#     for i in range(mid, n):
#         if s[i] == ch:
#             count += 1
#         else:
#             break
#     ans = count*2
#     if n%2 == 0:
#         print(ans)
#     else:
#         print(ans-1)
    



    
# def good_string():
#     # n = int(input())

#     s = input()
#     s_list = list(set(s))
#     if len(s) == len(s_list):
#         if len(s) % 2 == 1:
#             print('1')
#             # print(s[:-1])
#         else:
#             print("0")
#             # print(s)
#         return


#     ans = ''
#     steps = 0
#     l = 0
#     r = 1
    
#     while r < len(s):
#         while r < len(s) and s[l] != s[r]:
#             r += 1
#             steps += 1

#         if r < len(s): 
#             ans += s[l] + s[r]
#             l = r+1
#             r = l+1
#         if r== len(s):
#             ans += s[l]
#     if len(ans) % 2 == 1:
#         steps += 1
#         ans = ans[:-1]
#     print(steps)
#     # print(ans)

# # good_string()
# t = int(input())
# for _ in range(t):
#     # s = input()
#     good_string()


# t = int(input())
# for _ in range(t):
#     s = input().strip()
    
#     res = 0
#     last = '?'
#     need = 0
    
#     for c in s:
#         if need == 0:
#             last = c
#             need = 1
#         else:
#             if c == last:
#                 res += 2
#                 need = 0
    
# #     print(len(s) - res)
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     s = input().strip()
    
#     if s.count('T') != 2 * s.count('M'):
#         print("NO")
#         continue
    
#     c = 0
#     ok = True
#     for ch in s:
#         if ch == 'T':
#             c += 1
#         else:
#             c -= 1
#         if c < 0:
#             ok = False
    
#     c = 0
#     for ch in reversed(s):
#         if ch == 'T':
#             c += 1
#         else:
#             c -= 1
#         if c < 0:
#             ok = False
    
#     print("YES" if ok else "NO")


# n = int(input())

# e = {}

# for _ in range(n):
#     l,r = map(int,input().split())
#     e[l] = e.get(l,0) + 1
#     e[r+1] = e.get(r+1,0) - 1

# keys = sorted(e.keys())

# cnt = [0]*(n+1)

# cur = 0

# for i in range(len(keys)-1):
#     cur += e[keys[i]]
#     length = keys[i+1] - keys[i]
#     if cur > 0:
#         cnt[cur] += length

# print(*cnt[1:])

