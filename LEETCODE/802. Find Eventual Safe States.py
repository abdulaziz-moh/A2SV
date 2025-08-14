class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        dependency = [[] for _ in range(len(graph))]
        safecount = [0] * len(graph)
        safenodes = []

        for i, val in enumerate(graph):
            if not val:
                safenodes.append(i)
                safecount[i] = 0
            else:
                safecount[i] = len(val)

            for j in val:
                dependency[j].append(i)
        for j in safenodes:
            for val in dependency[j]:
                safecount[val] -= 1
                if safecount[val] == 0:
                    safenodes.append(val)
       
        return sorted(safenodes)
