class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        notecount = Counter(ransomNote)
        mgzncount = Counter(magazine)

        for k,v in notecount.items():
            if v > mgzncount[k]:
                return False
        return True