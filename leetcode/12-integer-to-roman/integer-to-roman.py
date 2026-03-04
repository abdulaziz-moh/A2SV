class Solution:
    def intToRoman(self, num: int) -> str:

        hm = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I' }
        ans = []
        
        for k,v in hm.items():
            
            while num >= k:
                ans.append(v)
                num -= k
            if num == 0:
                break

        return "".join(ans)         