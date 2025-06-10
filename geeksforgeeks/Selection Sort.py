#User function Template for python3

class Solution: 
    def selectionSort(self, arr):
        #code here
        length =  len(arr)

        for i in range(length -1):
            min_index = i

            for j in range(i+1, length):
                if arr[min_index] > arr[j]:
                    min_index = j
            if min_index != i:
                arr[i],arr[min_index] = arr[min_index] ,arr[i]

        return arr

