
def reverse(s):
    if len(s) == 1:
        return s
    return reverse(s[1:]) + s[0]

print(reverse("abcde"))

# def countDown(n, arr):
#     if n == 0:
#         return 0
#     a = countDown(n-1, arr)
#     arr.append(a)
#     return a+1
# arr = []
# countDown(10, arr)
# arr.append(10)
# print(arr)

def countDown(n, arr):
    arr.append(n)
    if n == 0:
        return
    return countDown(n-1, arr)

arr = []
countDown(10, arr)
# arr.append(10)
print(arr)