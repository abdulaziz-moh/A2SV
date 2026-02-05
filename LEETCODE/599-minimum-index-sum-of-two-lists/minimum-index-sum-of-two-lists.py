class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        hm = {}
        for i in range(len(list1)):
            hm[list1[i]] = i
        ans = []
        mn = float("inf")
        for i in range(len(list2)):
            if list2[i] in hm:
                if i+hm[list2[i]] == mn:
                    ans.append(list2[i])
                elif mn > i+hm[list2[i]]:
                    ans = [list2[i]]
                    mn = i+hm[list2[i]]
        return ans