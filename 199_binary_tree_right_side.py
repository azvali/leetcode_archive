def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
            
    if not root:
        return []

    q = deque([root])
    res = []

    while q:
        qlen = len(q)

        for _ in range(qlen):
            curr = q.pop()
            if curr.left:
                q.appendleft(curr.left)
            if curr.right:
                q.appendleft(curr.right)
        res.append(curr.val)

    return res