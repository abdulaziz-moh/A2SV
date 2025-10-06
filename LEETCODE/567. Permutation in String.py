import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        if len1 > len2:
            return False
        target = collections.Counter(s1)
        count_hm = collections.Counter(s2[:len1])
        if target == count_hm:
            return True
        for i in range(len1,len2):
            count_hm[s2[i]] += 1
            count_hm[s2[i-len1]] -= 1
            if count_hm[s2[i-len1]] == 0:
                del count_hm[s2[i-len1]]
            if count_hm == target:
                return True
        return False