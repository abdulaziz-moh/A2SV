def checksorted(arr):
    l,r = 0,1
    while r < len(arr):
        if arr[l] > arr[r]:
            return False
        l += 1
        r += 1
    return True

def mergesort(arr1,arr2):
    l,r = 0,0
    ans = []
    s1,s2 = len(arr1),len(arr2)
    while l < s1 and r < s2:
        if arr1[l] < arr2[r]:
            ans.append(arr1[l])
            l += 1
        # elif arr1[l] == arr2[r]:
        #     ans.append(arr1[l])
        #     ans.append(arr1[l])
        #     l += 1
        #     r += 1
        else:
            ans.append(arr2[r])
            r += 1
    ans.extend(arr1[l:])
    ans.extend(arr2[r:])
    return ans
arr1 = [1,2,3,3,4]
arr2 = [1,2,3,4]
# print(checksorted(arr1))
print(mergesort(arr1,arr2))

