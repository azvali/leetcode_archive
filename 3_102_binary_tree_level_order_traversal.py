def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    
    if not root:
        return []

    q = deque([root])
    res = []

    while q:
        lenq = len(q)
        temp = []

        for _ in range(lenq):
            curr = q.popleft()
            temp.append(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        
        res.append(temp)

    
    return res