class Solution:
    def decodeString(self, s: str) -> str:
        number = set(['0','1','2','3','4','5','6','7','8','9'])
        stack, temp, n = [], [], len(s)

        for v in s:
            if v != ']':
                stack.append(v)
            else:
                while stack and stack[-1] != '[':
                    temp.append(stack.pop())
                stack.pop()
                word = "".join(temp[::-1])
                temp = []
                x, num = 0, 0
                while stack and stack[-1] in number:
                    num += int(stack.pop()) * (10 ** x)
                    x += 1
                stack.append( num * word )
        return "".join(stack)