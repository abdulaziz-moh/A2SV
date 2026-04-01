class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hm = {'2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'], '5': ['j','k',
        'l'], '6': ['m','n','o'], '7': ['p','q','r','s'], '8': ['t','u','v'], '9': ['w','x','y','z']}
        ans, n = [], len(digits)
        def backtrack(ch, i):
            nonlocal ans
            if i >= n:
                ans.append(ch[:])
                return 

            for v in hm[digits[i]]:
                ch.append(v)
                backtrack(ch[:], i + 1)
                ch.pop()
        backtrack([], 0)
        submit = []
        for v in ans:
            submit.append("".join(v))
        return submit