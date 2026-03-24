class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        count = 0
        right = 0
        for v in nums:
            while right+1 < v:
                right += (right + 1)
                count += 1
                if right >= n:
                    break
            right += v
            if right >= n:
                break
        while right < n:
            right += (right + 1)
            count += 1
            
        return count
            
