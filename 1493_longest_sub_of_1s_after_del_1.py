def longestSubarray(nums: List[int]) -> int:

    count0 = 0
    l = 0
    res = 0
    
    for r in range(len(nums)):
        if nums[r] == 0:
            count0 += 1
            
        while count0 > 1:
            if nums[l] == 0:
                count0 -= 1
            l += 1
            
        res = max(res, r - l)

    return res