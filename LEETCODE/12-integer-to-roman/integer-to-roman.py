class Solution:
    def intToRoman(self, num: int) -> str:
        n = len(str(num))
        decim = [0]*n
        for i in range(1,n+1):
            decim[n-i] = num%10
            num //= 10

        hm = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        ans = []
        for i in range(1,n+1):
            p = 10**(n-i)
            if decim[i-1] == 4:
                ans.append(hm[p])
                ans.append(hm[p*5])
            elif decim[i-1] == 9:
                ans.append(hm[p])
                ans.append(hm[p*10])
            elif decim[i-1] == 1 or decim[i-1] == 5:
                ans.append(hm[p*decim[i-1]])
            else:
                r = decim[i-1]//5
                rem = decim[i-1]%5
                if r: 
                    ans.append(hm[p*5])
                for _ in range(rem):
                    ans.append(hm[p])
        return "".join(ans)         