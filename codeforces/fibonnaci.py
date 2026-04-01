

# def fibonaci(n, hm):
#     if n == 0:
#         hm[n] = 0
#         return 0
#     elif n == 1:
#         hm[n] = 1
#         return 1
#     x = fibonaci(n-1, hm) + fibonaci(n-2,hm)
#     hm[n] = x
#     return x
# hm = {}
# fibonaci(10,hm)    
# for i in range(11):
#     print(hm[i], end=" ")
    

def fibonaci(n, hm):
    if n == 0:
        hm[n] = 0
        return 0
    elif n == 1:
        hm[n] = 1
        return 1
    if n-1 in hm:
        a = hm[n-1]
        b = hm[n-2]
        x = a+b
    else:
        x = fibonaci(n-1, hm) + fibonaci(n-2,hm)
    hm[n] = x
    return x
hm = {}
fibonaci(10,hm)    
for i in range(11):
    print(hm[i], end=" ")