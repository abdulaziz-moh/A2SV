class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
    

        stack = False
        tempstatus = False
        ans = []
        temp = []
        for line in source:

            n = len(line)
            lastidx = n
            start = 0

            i = 0
            while i < n:

                if not stack and line[i] == '/' and i < n - 1:
                    if line[i+1] == '/':
                        lastidx = i
                        break
                    elif line[i+1] == '*':
                        if line[start:i]:
                            temp.append(line[start:i])
                            # temp = line[start:i]
                            tempstatus = True
                        stack = True
                        i += 1
                elif stack and line[i] == '*' and i < n-1:
                    if line[i+1] == '/':
                            stack = False
                            start = i+2
                            i += 1
                i += 1
            if not stack and tempstatus:
                # ans.append(temp + line[start:lastidx])
                ans.append("".join(temp) + line[start:lastidx])
                tempstatus = False
                temp = []
            elif not stack and line[start:lastidx]:
                ans.append(line[start:lastidx])

        return ans