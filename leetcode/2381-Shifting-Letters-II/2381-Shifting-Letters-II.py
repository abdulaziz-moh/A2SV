class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0]*(n+1)

        for l,r,d in shifts:
            if d == 0:
                prefix[l] -= 1
                prefix[r+1] += 1
            else:
                prefix[l] += 1
                prefix[r+1] -= 1
        for i in range(1,n):
            prefix[i] += prefix[i-1]
        ans = []
        offset = ord('a')
        for i in range(n):
            num = ord(s[i]) - offset
            num = (num + prefix[i]) % 26 + offset
            ans.append(chr(num))
        return "".join(ans)