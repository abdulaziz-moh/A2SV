class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        for v in s:
            if v == '(':
                stack.append('(')
            else:
                if stack[-1] == "(":
                    stack.pop()
                    val = 1
                    if stack and stack[-1].isdigit():
                        val = int(stack[-1]) + 1
                        stack.pop()
                    stack.append(str(val))
                else:
                    val = int(stack.pop()) * 2
                    stack.pop()
                    if stack and stack[-1].isdigit():
                        val = int(stack[-1]) + int(val)
                        stack.pop()
                    stack.append(str(val))
            
        for v in stack:
            if not v.isdigit():
                return
            ans += int(v)
        return ans      

