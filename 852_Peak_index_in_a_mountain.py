def function(arr):
    
    l, r = 0 , len(arr) - 1
    
    while l <= r:
        cur = (l + r) // 2
        
        if cur > 0 and arr[cur] < arr[cur + 1]:
            l = cur + 1
            continue
        if cur < len(arr) - 1 and arr[cur - 1] > arr[cur]:
            r = cur - 1
            continue
        
        return cur