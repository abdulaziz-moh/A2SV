class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for v in tokens:            
            if v == '+':
                n1 = int(stack.pop())
                stack.append(int(stack.pop()) + n1)
            elif v == '-':
                n1 = int(stack.pop())
                stack.append(int(stack.pop()) - n1)
            elif v == '*':
                n1 = int(stack.pop())
                stack.append(int(stack.pop()) * n1)
            elif v == '/':
                n1 = int(stack.pop())
                if n1 == 0:
                    return
                stack.append(int(stack.pop()) / n1)
            else:
                stack.append(v)
        return int(stack[0])