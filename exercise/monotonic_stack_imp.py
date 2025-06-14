height = [1,2,4,1,2,5,2,44]
length = len(height)
next_highest = [-1] * length


my_stack = []
top = 0
print(next_highest)

for i in range(length-1,-1,-1):
    while len(my_stack) != 0 and height[i] <= my_stack[top]:
        my_stack.pop()
        top -= 1
