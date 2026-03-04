class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        wcount1 = Counter(word1)
        wcount2 = Counter(word2)

        if wcount1.keys() != wcount2.keys():
            return False

        # count of -- result of counter
        val1 = defaultdict(int)
        val2 = defaultdict(int)
        for v in wcount1.values():
            val1[v] += 1
        for v in wcount2.values():
            val2[v] += 1

        if val1 == val2:
            return True
        return False
