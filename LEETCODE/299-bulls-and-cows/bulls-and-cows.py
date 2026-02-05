class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = 0
        hm = {}
        for v in secret:
            if v in hm:
                hm[v] += 1
            else:
                hm[v] = 1
        for v in guess:
            if v in hm and hm[v] > 0:
                hm[v] -= 1
                cow += 1
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
        return (str(bull) + 'A' + str(cow-bull) + 'B')                
            