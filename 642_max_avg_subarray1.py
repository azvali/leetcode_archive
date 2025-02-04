def findMaxAverage(nums: List[int], k: int) -> float:

    sum = 0
    l, r = 0, 0
    
    while r < k:
        sum += nums[r]
        r += 1
    
    res = sum / k
    
    while r < len(nums):
        sum += nums[r]

        res = max(res, sum/k)
        sum -= nums[l]
        l += 1
        r += 1
        

    return res