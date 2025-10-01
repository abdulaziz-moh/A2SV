from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i, ch in enumerate(s):
            last_index[ch] = i
        left = 0
        right = -1
        length = len(s)
        ans = []
        i = 0
        while i < length:
            right = last_index[s[left]]
            count = 1
            while i < right:
                if s[i] != s[left]:
                    # print("i: ",i," left: ",left)
                    right = max(right,last_index[s[i]])
                i += 1
                count += 1
                # print("i:  ",i,"         count: ",count)
            i += 1
            ans.append(count)
            left = i
        # print(ans)
        return ans
    
obj = Solution()
s = "ababcbacadefegdehijhklij"
obj.partitionLabels(s)

# from typing import List
# class Solution:
#     def partitionLabels(self, s: str) -> List[int]:

#         last_index = {}
#         for i, ch in enumerate(s):
#             last_index[ch] = i
        
#         left = 0
#         right = -1
#         length = len(s)
#         ans = []
        
#         while right < length:
            

#             left = right + 1
#             start = left-1
#             right = last_index[s[left]]
            
#             while left < right:
#                 left +=1
#                 if last_index[s[left]] > right:
#                     right = last_index[s[left]]
                       
#             ans.append(right - start)
#             if right == length -1:
#                 break 
#         return ans


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        htable = {}
        newnum = list(nums) 
        sorted_nums = sorted(nums)
        length = len(sorted_nums)
        count = 0
        x = sorted_nums[0]
        for v in sorted_nums:
            if v == x:
                htable[v] = count
            else:
                x = v
                count += 1
                htable[v] = count