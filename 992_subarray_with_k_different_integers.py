def subarraysWithKDistinct(nums: List[int], k: int) -> int:
    
    
    def atmost(k):
        
        hashmap = {}
        l = 0
        res = 0
        
        for r in range(len(nums)):
            hashmap[nums[r]] =  hashmap.get(nums[r], 0) + 1
            
            
            while len(hashmap) > k:
                hashmap[nums[l]] = hashmap.get(nums[l], 0) - 1
                if hashmap[nums[l]] == 0:
                    del hashmap[nums[l]]
                l += 1
                
            res += r - l + 1
            
        return res
    
    
    return atmost(k) - atmost(k - 1)
    