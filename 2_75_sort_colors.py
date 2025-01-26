def sortColors(nums: List[int]) -> None:
    
    
    l, r = 0, len(nums) - 1
    x = 0
    
    while x <= r:
        if nums[x] == 0:
            nums[l], nums[x] = nums[x], nums[l]
            l += 1
            x += 1
        elif nums[x] == 2:
            nums[r] , nums[x] = nums[x], nums[r]
            r -= 1
            continue
        else:
            x += 1