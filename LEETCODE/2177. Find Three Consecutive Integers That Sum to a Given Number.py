class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        output = []

        
        if num % 3 == 0:
            x = int(num/3)
            output.append(x-1)
            output.append(x)
            output.append(x+1)

        return output