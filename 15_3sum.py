def threeSum(nums):
    nums.sort()
    res = []
    
    for x in range(len(nums)):
        
        if x > 0 and nums[x] == nums[x - 1]:
            continue
            
        l, r = x + 1 , len(nums) - 1
        
        while l < r: 
            
            cur = nums[x] + nums[l] + nums[r]

            if cur > 0:
                r -= 1
            elif cur < 0:
                l += 1
            else:
                res.append([nums[x], nums[l], nums[r]])
                l += 1
                r -= 1
            
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1

            
        
    return res