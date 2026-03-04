class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n_row = len(img)
        n_col = len(img[0])
        ans = [[0]*n_col for _ in range(n_row)]  # correct way to create a 2d array

        # for mid elements (with 8 neibours)
        for i in range(n_row):
            for j in range(n_col):
                count = 0
                sum = 0
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if 0 <= k < n_row and 0 <= l < n_col:
                            sum += img[k][l]
                            count += 1
                ans[i][j] = sum//count

        return ans