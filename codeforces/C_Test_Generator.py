t = int(input())
for _ in range(t):
    s, m = map(int,input().split())
    
    bit = format(m, 'b')
    n = len(bit)
    idx, sum = [], 0
    
    for i in range(len(bit)):
        if bit[i] == '1':
            idx.append(n-i-1)
            sum += (2**(idx[-1]))
    nums = [m]
    sset = set()
    set.add(m)
    for v in idx:
        sum -= (2**v)
        nums.append(sum)
        sset.add(sum)
    nums.sort()
    for i in range(len(nums)):
        sum = s - nums[i]  #untill num of i
        if sum == 0:
            # print(dadfdsfasfadsfsd)
            break
        elif sum < 0:
            continue
        else:
            if sum in sset:
                # print(dadfdsfasfadsfsd)
                break
            