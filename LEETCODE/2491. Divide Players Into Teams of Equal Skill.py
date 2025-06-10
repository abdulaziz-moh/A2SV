from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill.sort()
        left = 1
        right = len(skill) - 2
        eq_sum = skill[0] + skill[right+1]
        chem = skill[0] * skill[right+1]
        while left < right:
            if (skill[left] + skill[right]) == eq_sum:
                chem += skill[left] * skill[right]
                left += 1
                right -= 1
            else:
                return -1
        return chem



        