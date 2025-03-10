def findDuplicate(self, nums: List[int]) -> int:
            
    slow, fast = nums[0], nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
            
    newslow = nums[0]
    while newslow != slow:
        newslow = nums[newslow]
        slow = nums[slow]

    return newslow