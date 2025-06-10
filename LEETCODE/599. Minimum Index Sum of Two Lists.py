class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        length1 = len(list1)
        length2 = len(list2)
        result =[]
        min_index_sum = float('inf')

        for i in range(length1):
            for j in range(length2):

                if list1[i] == list2[j]:
                    sum = i+j
                    if sum < min_index_sum:
                        result = [list1[i]]
                        min_index_sum = sum
                    elif sum == min_index_sum:
                        result.append(list1[i])
                    break
        return result