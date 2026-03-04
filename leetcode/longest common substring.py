class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
# def longestCommonPrefix(strs):
        hm = {}
        length = len(strs)
        for strr in strs:
            hm[strr] = {}            
            for ch in strr:
                hm[strr][ch] = 1
        count = [[]]
        i=0
        contin = True
        status = True
        for ch in strs[0]:
            if status:
                contin = True
            else:
                contin = False
            status = True

            for strr in strs:
                if status and ch in hm[strr] and hm[strr][ch] == 1:
                    continue
                else:
                    status = False
                    break
            if status and contin:
                count[i].append(ch)
            elif status and not contin:
                i+=1
                count.append([])
                count[i].append(ch)
        print(''.join(max(count, key=len)))
     
# strs = ["flower","flow","flight"]
# longestCommonPrefix(strs)
