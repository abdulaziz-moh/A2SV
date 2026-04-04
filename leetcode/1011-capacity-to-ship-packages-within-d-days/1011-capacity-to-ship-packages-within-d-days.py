class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:


            def check(mid):
                count, sm = 0, 0
                for v in weights:
                    sm += v
                    if sm > mid:
                        count += 1
                        sm = v
                count += 1

                if count <= days:
                    return True
                return False

            left, right = max(weights), sum(weights)
            while left <= right:
                mid = (left + right) // 2
                if check(mid):
                    right = mid - 1
                else:
                    left = mid + 1
            return right + 1
















        
        # def check_valid_capacity(num):
        #     count = 0
        #     sum = 0
        #     for v in weights:
        #         sum += v
        #         status = True
        #         if sum == num:
        #             count += 1
        #             sum = 0
        #         elif sum > num:
        #             count += 1
        #             sum = v
        #             status = False

        #         else:
        #             status = False
        #     if not status:
        #         count += 1
        #     if count <= days:
        #         return True
        #     return False

        # left, right = max(weights), sum(weights)
        # while left <= right:
        #     mid = (left + right) // 2
        #     # print(left, " ", mid, " ", right)
        #     if check_valid_capacity(mid):
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return right + 1

        