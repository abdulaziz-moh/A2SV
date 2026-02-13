class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row = len(img)
        col = len(img[0])
        new_arr = [[0]*col for _ in range(row)]
        moves = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        
        for i in range(row):
            for j in range(col):
                count, sum = 1, img[i][j]
                for x,y in moves:
                    ni = i + x
                    nj = j + y
                    if ni > -1 and nj > -1 and ni < row and nj < col:
                        count += 1
                        sum += img[ni][nj]
                new_arr[i][j] = sum//count
        return new_arr