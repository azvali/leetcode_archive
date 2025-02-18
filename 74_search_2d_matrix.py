def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
    t , b = 0 , len(matrix) - 1
    cur = 0
    
    while t <= b:
        cur = t + (b - t) // 2
        
        if target > matrix[cur][-1]:
            t = cur + 1
        elif target < matrix[cur][0]:
            b = cur - 1
        else:
            break
        
    l , r = 0 , len(matrix[0]) - 1

    while l <= r:
        mid = l + (r - l) // 2
        
        if target > matrix[cur][mid]:
            l = mid + 1
        elif target < matrix[cur][mid]:
            r = mid - 1
        else:
            if matrix[cur][mid] == target:
                return True
            
    return False