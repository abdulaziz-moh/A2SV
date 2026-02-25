def ArrayChallenge(arr):
  arr.sort()
  length = len(arr)
  count, mx = 0, 0

  for i in range(length-1):
    if arr[i] + 1 == arr[i+1]:
      count += 1
      mx = max(count+1, mx)
    else:
      count = 0

  # code goes here
  return mx

arr = [5, 6, 1, 2, 8, 9, 7]
# arr = [1,3,6,6,7,12,100,102]
# keep this function call here 
print (ArrayChallenge(arr))