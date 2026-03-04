class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        ans = []
        hm = {}

        for domain in cpdomains:
            num = []
            for v in domain:
                if v == ' ':
                    break
                num.append(v)
            count = int("".join(num))

            for i in range(len(domain)-1,-1,-1):
                if domain[i] == '.':
                    subd = domain[i+1:]
                    if subd in hm:
                        hm[subd] += count
                    else:
                        hm[subd] = count
                elif domain[i] == ' ':
                    subd = domain[i+1:]
                    if subd in hm:
                        hm[subd] += count
                    else:
                        hm[subd] = count
                    break
        for key,value in hm.items():
            ans.append(str(value) + " " + key)
        return ans
