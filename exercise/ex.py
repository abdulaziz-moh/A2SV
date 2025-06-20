

b = "Hello, World"
print(b[2])   
print(b[-3]) 
print(b[2:5])
print(b[:5])  
print(b[2:])  
print(b[5:2:-1])  
print(b[::-1])  
print(b[::2])

for num in range(10,14):
    for i in range(2, num):
        if num % i == 1:
            print(num)
            break

class Solution:
    def isPalindrome(self, x: int) -> bool:
        val = str(x)
        aval = val[::-1]
        if val == aval:
            return True
        else:
            return False
        