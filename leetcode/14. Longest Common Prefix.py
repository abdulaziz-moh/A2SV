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

# This is more optimized version(in both time and memory)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        try:
            i = -1
            for ch in strs[0]:
                i += 1
                for val in strs:  # we used for-else block to avoid using a status(boolean variable), because it automatically checks if the break is used or not
                    if val[i] != ch:
                        break
                else:
                    ans.append(ch)
                    continue
                break
            return ("".join(ans))
        except IndexError:    # help us catch if the first element is not the minumum length element, by raising an exception when trying to access element in length of first string but not others
            return ("".join(ans))