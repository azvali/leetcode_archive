def function(arr):
    
    l, r = 0 , len(arr) - 1
    
    while l < r:
        cur = (l + r) // 2
        
        if arr[cur] < arr[cur + 1]:
            l = cur + 1
            continue
        else:
            r = cur

        
    return l