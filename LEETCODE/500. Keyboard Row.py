from collections import Counter
from typing import List
class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        firstw = Counter("qwertyuiop")
        secondw = Counter("asdfghjkl")
        thirdw = Counter("zxcvbnm")
        status = True
        ans = []

        length = len(words)
        for i in range(length):
            status = True
            
            if words[i][0].lower() in firstw:
                hmcheck = firstw
            elif words[i][0].lower() in secondw:
                hmcheck = secondw
            else: hmcheck =thirdw

            len_i = len(words[i])
            
            for j in range (1,len_i):
                if words[i][j].lower() not in hmcheck:
                    status = False
                    break
            if status:
                ans.append(words[i])

        return ans