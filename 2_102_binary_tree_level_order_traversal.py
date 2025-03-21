def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    queue = deque([root])
    res = []

    while queue:
        n = len(queue)
        temp = []
        for _ in range(n):
            i = queue.popleft()
            temp.append(i.val)
            if i.left:
                queue.append(i.left)
            if i.right:
                queue.append(i.right)
        
        res.append(temp)
    
    return res