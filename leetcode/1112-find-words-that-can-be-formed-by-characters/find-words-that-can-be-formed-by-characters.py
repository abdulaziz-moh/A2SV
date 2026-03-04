class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        hm = {}
        for ch in chars:
            if ch in hm:
                hm[ch] += 1
            else:
                hm[ch] = 1

        ans = 0
        for word in words:
            count = {}
            for c in word:
                if c in count:
                    count[c] += 1
                else:
                    count[c] = 1
            for v in count:
                if v not in hm or count[v] > hm[v]:
                    break
            else:
                ans += len(word)
        return ans


