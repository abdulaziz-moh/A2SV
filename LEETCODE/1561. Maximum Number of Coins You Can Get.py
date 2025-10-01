class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # [1,2,2,4,7,8]
        # we are asked to find the max sum from a selection of 3-3 piles and taking the middle element
        # we know the first person take the max, the second(me) take the mid , and the third take the min
        # now, because we have 3*n elements each person takes n-elements and the efficient approch will be
        #  the 3rd person takes the first n-min elements(for me to get the max)
        #  me and the third person will take one element after another(while i take one min then he get max then me and so.)
        piles.sort()
        l = len(piles)
        i = l//3
        sum = 0
        while i < l:
            sum += piles[i]
            i += 2
        return sum