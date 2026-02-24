class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chemistry = skill[0] * skill[-1]
        sum = skill[0] + skill[-1]
        left, right = 1, len(skill) - 2

        while left < right:
            x = skill[left] + skill[right]
            if x != sum:
                return -1
            chemistry += (skill[left] * skill[right])
            left += 1
            right -= 1
        return chemistry
