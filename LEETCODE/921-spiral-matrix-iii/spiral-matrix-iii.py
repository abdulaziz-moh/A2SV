class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        hm = {0:[0,1], 1:[1,0], 2:[0,-1] ,3:[-1,0]}
        ans = [[rStart,cStart]]
        x, y = ans[0]
        totalgrid = rows*cols
        k, cnt = 1.0, 0
        while len(ans) < totalgrid:
            dxn = hm[cnt%4]
            for _ in range(int(k)):
                x += dxn[0]
                y += dxn[1]
                if 0 <= x < rows and 0<= y < cols:
                    ans.append([x,y])
            cnt += 1
            k += 0.5
        return ans

