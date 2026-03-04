class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        hm = {}
        ans = []
        for path in paths:
            fp = []
            f = []
            filename = ""
            

            for ch in path:
                # print(ch)
                if ch == '/' or (ch == " " and f):
                    fp.append("".join(f))
                    f = []
                elif ch == '(':
                    filename = "".join(f)
                    f = []
                elif ch == ')':
                    k = "".join(f)
                    if k in hm:
                        hm[k].append("/".join(fp)+ "/" + filename)
                    else:
                        hm[k] = ["/".join(fp) + "/" + filename]
                    f = []
                elif ch == " " and not f:
                    continue
                else:
                    f.append(ch)
        for v in hm.values():
            if len(v) > 1:
                ans.append(v)
        return ans