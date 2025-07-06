

# b = "Hello, World"
# print(b[2])   
# print(b[-3]) 
# print(b[2:5])
# print(b[:5])  
# print(b[2:])  
# print(b[5:2:-1])  
# print(b[::-1])  
# print(b[::2])

# for num in range(10,14):
#     for i in range(2, num):
#         if num % i == 1:
#             print(num)
#             break

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         val = str(x)
#         aval = val[::-1]
#         if val == aval:
#             return True
#         else:
#             return False
        

nums = [1,2,3,4,5,6,7,8,9]

even_nums = [i for i in nums if i % 2 == 0]
print(even_nums)
my_list = [[0]] * 5     # Creates a 2D array with each arry have same memory location(but different reference(only for 2d not for 1d))
my_list[3][0] = 2       # changing one affects all
print(my_list)          # output    [[2], [2], [2], [2], [2]]    

# So for creating 2D array use this below instead:
my_2d_indepnedent_list = [[0] for _ in range(5)]        # Creates a 2D array with each arry have different memory location
my_2d_indepnedent_list[3][0] = 2        # changing one affects only that one
print(my_2d_indepnedent_list)           # output  [[0], [0], [0], [2], [0]]

dictionary = {num:num ** 2 for num in range(10) if num%2 == 0} 
print(dictionary)

print("Keys only:")
for key in dictionary:  # Iterating over keys in dictionary
    print(key)

print("Values only: ")
for value in dictionary.values():   # Iterating over values in dictionary
    print(value)

print("Key - value pair: ")
for key, value in dictionary.items():   # Iterating over both key:value in dictionary
    print(f"{key}: {value}")

original_dict = {'key1': ['value1'], 'key2': 'value2'}
shallow_copied_dict = original_dict.copy()    # In a Shallow Copy it does not create new copies of the objects inside the dictionary but referece to the original objects
                                              # So Changes made to mutable objects (like lists) within the original dictionary will affect the corresponding objects in the copied dictionary, and vice versa.
                                              # But note that for basic data types their copy created and not referenced to the data on the original data
original_dict['key1'].append('value3')
original_dict['key2'] = 'value4'
print(shallow_copied_dict)  # Output?  {'key1': ['value1', 'value3'], 'key2': 'value2'}