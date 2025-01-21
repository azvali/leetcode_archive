def findDuplicate(nums: List[int]) -> int:
    
    
    slow = 0
    fast = 0
    
    while True:
        slow = nums[slow]
        fast = nums[nums[slow]]
    
        if slow == fast:
            break
        
        
    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        
        if slow == slow2:
            return slow