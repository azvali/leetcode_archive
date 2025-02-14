def search(self, nums: List[int], target: int) -> int:


    def findpivot(arr):
        l , r = 0 , len(arr) - 1
        cur = l + (r - l) //2

        while nums[cur] > nums[cur - 1]:
            if nums[cur] > nums[r]:
                l = cur + 1
            else:
                r = cur - 1
            
            cur = l + (r - l) // 2
        return cur

    pivotindex = findpivot(nums)
    l , r = 0 , len(nums) - 1

    if target <= nums[r]:
        l , r = pivotindex , len(nums) - 1
    else:
        l , r = 0 , pivotindex - 1

    while l <= r:
        mid = l + (r - l) // 2

        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            return mid

    return -1