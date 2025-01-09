def productExceptSelf(nums: List[int]) -> List[int]:
    
    
    prefixprod = [1] * len(nums)
    postfixprod = [1] * len(nums)
    res= []

    totalprod = 1
    for x in range(len(nums)):
        
        prefixprod[x] = totalprod
        totalprod *= nums[x]
        
    totalprod = 1
    
    for x in range(len(nums) - 1, -1, -1):
        
        postfixprod[x] = totalprod
        totalprod *= nums[x]
        
        
    for i in range(len(nums)):
        
        res.append(prefixprod[i] * postfixprod[i])
        
    return res
        
            


        
        