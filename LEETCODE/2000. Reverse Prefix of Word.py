class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        ans = []

        for v in word:
            stack.append(v)
            if v == ch:
                break
        if stack[-1] != ch:
            return word
        i = 0
        while stack:
            ans.append(stack.pop())
            i += 1
        while i < len(word):
            ans.append(word[i])
            i += 1
        return "".join(ans)