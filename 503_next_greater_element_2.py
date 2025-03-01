def nextGreaterElements(self, nums: List[int]) -> List[int]:
    res = [-1] * len(nums)
    stack = []

    for x in range(len(nums) * 2):
        while stack and nums[stack[-1]] < nums[x % len(nums)]:
            res[stack.pop()] = nums[x % len(nums)]
        
        if x < len(nums):
            stack.append(x)
    
    return res