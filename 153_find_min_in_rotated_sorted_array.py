def findMin(self, nums: List[int]) -> int:
    

    l , r = 0, len(nums) - 1
    cur = l + (r - l) // 2

    while l < r:
        cur = l + (r - l) // 2

        if nums[cur] > nums[r]:
            l = cur + 1
        else :
            r = cur 
    
    return nums[l]
