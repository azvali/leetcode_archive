import queue as q


def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    queue = q.Queue()
    queue.put(root)
    res = []
    
    while not queue.empty():
        temp = []
        lenq = queue.qsize()
        
        for _ in range(lenq):
            n = queue.get()

            temp.append(n.val)
            if n.left:
                queue.put(n.left)
            if n.right:
                queue.put(n.right)

        res.append(temp)
    
    return res