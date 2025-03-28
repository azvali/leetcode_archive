def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:


    stack = []
    res = 0
    curr = root

    while True:
        while curr:
            stack.append(curr)
            curr = curr.left

        
        curr = stack.pop()
        res += 1
        if res == k:
            return curr.val
        curr = curr.right
        