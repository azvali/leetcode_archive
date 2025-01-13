def longest_consecutive(nums: list[int]) -> int:
    
    hashset = set(nums)
    res = 0
    cur = 0
    
    for x in hashset:
        
        if x - 1 not in hashset:
            cur = 1

            while x + cur in hashset:
                cur += 1
            
            res = max(res, cur)
                    
    return res

        
        
            
        