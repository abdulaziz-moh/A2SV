class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        splited_s = s.split()
        hm = {}
        sset = set()
        if len(pattern) == len(splited_s):
            for i in range(len(pattern)):
                if pattern[i] not in hm:
                    if splited_s[i] not in sset:
                        hm[pattern[i]] = splited_s[i]
                        sset.add(splited_s[i])
                    else:
                        return False
                else:
                    if splited_s[i] != hm[pattern[i]]:
                        return False
            return True
        return False