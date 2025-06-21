class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
# def longestCommonPrefix(strs):

        min_str  = strs[0]
        for val in strs:
            if len(val) < len(min_str):
                min_str = val


        ans = []
        i = -1
        status = True
        for ch in min_str:
            i += 1
            for val in strs:
                if val[i] != ch:
                     status = False
                     break
            if status:
                 ans.append(ch)
            else:
                 break
        
        print(''.join(ans))
    

# strs = ["flower","flow","flight"]
# longestCommonPrefix(strs)
