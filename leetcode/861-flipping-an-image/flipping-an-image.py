class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        l = len(image[0])
        n = math.ceil(l/2)
        
        for arr in image:
            for i in range(n):
                if arr[i] == arr[l - i - 1]:
                    arr[i], arr[l - i - 1] = abs(arr[i] - 1), abs(arr[i] - 1)
        return image