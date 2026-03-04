class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cor = []
        safecount = [0] * numCourses
        dependency = [[] for _ in range(numCourses)]

        for a,b in prerequisites:
            cor.append(a)
            safecount[a] += 1
            dependency[b].append(a)

        independent = []
        for i in range(numCourses):
            if i not in cor:
                independent.append(i)
    
        for i in independent:
            for j in dependency[i]:
                safecount[j] -= 1
                if safecount[j] == 0:
                    independent.append(j)
        if len(independent) == numCourses:
            return independent
        else:
            return []

            