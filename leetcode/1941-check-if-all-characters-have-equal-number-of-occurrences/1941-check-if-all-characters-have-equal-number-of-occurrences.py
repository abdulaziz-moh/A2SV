class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = Counter(s)
        check = count[s[0]]
        for v in count.values():
            if v != check:
                return False
        return True