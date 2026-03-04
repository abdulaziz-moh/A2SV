from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l,chem,r = 0,0,len(skill) - 1
        sum  = skill[l] + skill[r]
        while l<r:
            if skill[l] + skill[r] == sum:
                chem += skill[l] +skill[r]
            else:
                return -1
            l += 1
            r -= 1
        return chem



        