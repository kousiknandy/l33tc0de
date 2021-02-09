def subset_sum(nums, target):
    M = sum(nums)
    m = [False] * (M+1)
    m[0] = True
    for i in range(len(nums)):
        for j in range(M, 0, -1):
            if j < nums[i]:
                break
            #print("i =", i, "j =", j, "nums[i] =", nums[i], j - nums[i], "m =", m[j], ",", m[j-nums[i]])
            m[j] |= m[j - nums[i]]
    #print(m[target], m)
    return m[target]

def candy_division(nums):
    M = sum(nums)
    m = [False] * (M+1)
    m[0] = True
    for i in range(len(nums)):
        for j in range(M, 0, -1):
            if j < nums[i]: break
            m[j] |= m[j - nums[i]]
    for i in range(M//2):
        if m[M//2 - i]:
            print("ideal", M//2, "actual", M//2-i)
            return M//2 - i

subset_sum([4, 5, 6, 9, 10, 13], 14)
candy_division([4, 5, 6, 9, 10, 13, 33])
