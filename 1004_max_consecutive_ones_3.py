def longestOnes(self, nums: List[int], k: int) -> int:
        
        
    res = 0
    count0s = 0
    l = 0

    for r in range(len(nums)):

        if nums[r] == 0: 
            count0s += 1
            
        while count0s > k:
            if nums[l] == 0:
                count0s -= 1
            l += 1
            
        res = max(res, r - l + 1)
            
    return res