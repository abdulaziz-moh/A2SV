# Inserting an element in an array (which is O(n))

my_list = [1,2,3,5,6,7,8,9,10]  # 4 missing
print(f"Befor: {my_list}")
num = int(input("enter the number: "))

length = len(my_list)
my_list.append(my_list[length-1])

for i in range(length-2,-1,-1):
    if num >= my_list[i]:
        my_list[i+1] = num
        break
    else:
        my_list[i+1] = my_list[i]
else:
    my_list[0] = num

print(f"After: {my_list}")

# Removing an element from list(which is 0(n))

num = int(input("enter the number to remove: "))
length = len(my_list)
for i in range(length):
    if num == my_list[i]:
        for j in range(i,length - 1):
            my_list[j] = my_list[j + 1]
        my_list.pop()
        break

else:
    print(f"Their is no element '{num}'")
print(my_list)

