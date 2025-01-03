def function(arr, target):
    l, r = 0, len(arr) - 1
    
    while l <= r:
        cur = (l + r) // 2
        
        if arr[cur] > target:
            r = cur - 1
            continue
        elif arr[cur] < target:
            l = cur + 1
            continue
    
        if arr[cur] == target:
            Lbound, Rbound = cur, cur
            
            while Lbound > 0 and arr[Lbound - 1] == target  :
                Lbound -= 1
                 
            while Rbound < len(arr) - 1 and arr[Rbound + 1] == target :
                Rbound += 1
                
            return [Lbound, Rbound]
        
    return [-1,-1]