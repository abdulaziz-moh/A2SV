class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        if len(changed) % 2 != 0:
            return []
        changed.sort()
        count = Counter(changed)
        ans  = []

        for v in changed:
            doubled = v*2
            if doubled in count and count[doubled] > 0 and count[v] > 0:
                ans.append(v)
                count[v] -= 1
                count[doubled] -= 1
                if count[v] < 0:
                    ans.pop()

        if len(ans) == len(changed)//2:
            return ans
        return []            