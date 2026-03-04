def partition(nums):
    pvot = nums[0]
    right_num,left_num = [],[]
    for num in nums[1:]:
        if num > pvot:
            right_num.append(num)
        else:
            left_num.append(num)
    return left_num, pvot, right_num

def quickSort(nums):
    if len(nums) <= 1:
        return nums
    left_num, pvot, right_num = partition(nums)
    return quickSort(left_num), [pvot], quickSort(right_num)
nums = [9,8,7,6,5,4,3,2,1]
print(quickSort(nums))