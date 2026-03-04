n = len(nums)
        hm = {0:-1}
        prefix = 0

        for i in range(n):
            prefix += nums[i]
            x = prefix % k
            if x in hm and i-hm[x] >= 2:
                return True
            if x not in hm:
                hm[x] = i
        return False