def search(self, nums: List[int], target: int) -> int:
    l , r = 0 , len(nums) - 1



    while l <= r:
        cur = l + (r - l) // 2
        
        if nums[cur] < target:
            l = cur + 1
        elif nums[cur] > target:
            r = cur - 1
        else:
            return cur
        
    return -1