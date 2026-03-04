class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0]*(n+1)
        ans = []
        for shift in shifts:
            add = 1
            if shift[2] == 0:
                add = -1
            prefix[shift[0]] += add
            prefix[shift[1]+1] -= add
        for i in range(1,n):
            prefix[i] += prefix[i-1]
        for i in range(n):
            chrnum = ord(s[i]) + prefix[i] % 26
            if chrnum > 122:
                chrnum = chrnum - 26
            elif chrnum < 97:
                chrnum = 26 + chrnum
            ans.append(chr(chrnum))
        return "".join(ans)