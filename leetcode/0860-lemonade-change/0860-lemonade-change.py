class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        price = deque()

        for v in bills:
            if v == 5:
                price.appendleft(v)
            if v == 10:
                if price and price[0] == 5:
                    price.popleft()
                    price.append(10)
                else:
                    return False
            elif v == 20:
                count = 20
                while price and count > 5:
                    if count > 10:
                        count -= price.pop()
                    else:
                        count -= price.popleft()
                if count != 5:
                    return False
        return True