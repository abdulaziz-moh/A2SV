class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
    
        stack = False  # False => we haven't encountered /* still    ||||| True => we have get /* befor (but not still */  when we get */ we will change it to False )
        tempstatus = False  # used to show their is a fragment of code to make them togather because they are separated by a multiline comment. e.g. int x = /*this is comment*/5 ;  now int x = 5 ;
        ans = []
        temp = []
        for line in source:
            
            i = 0
            n = len(line)
            startidx = 0
            lastidx = n
            while i < n:

                if not stack and line[i] == '/' and i < n - 1:
                    if line[i+1] == '/':
                        lastidx = i
                        break
                    elif line[i+1] == '*':
                        if line[startidx:i]:
                            temp.append(line[startidx:i])
                            tempstatus = True
                        stack = True
                        i += 1
                elif stack and line[i] == '*' and i < n-1:
                    if line[i+1] == '/':
                        stack = False
                        startidx = i+2
                        i += 1
                i += 1
            if not stack and tempstatus:
                ans.append("".join(temp) + line[startidx:lastidx])
                tempstatus = False
                temp = []
            elif not stack and line[startidx:lastidx]:
                ans.append(line[startidx:lastidx])

        return ans