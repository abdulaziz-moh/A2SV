class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        l,c,r = 0,0,len(people) - 1
        while l<=r:
            if people[l] + people[r] <= limit:
                l += 1
            c += 1
            r -= 1
        return c