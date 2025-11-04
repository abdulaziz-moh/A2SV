class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        l,r = n-1,n-1
        words = []

        while  l >= 0:
            while l >= 0 and s[l] == " ":
                l -= 1
            r = l + 1
            while l >= 0 and s[l] != " ":
                l -= 1
            words.append(s[l+1:r])
        if words[-1] == "":
            words.pop()
        return " ".join(words)