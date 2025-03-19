def goodNodes(self, root: TreeNode) -> int:
    if not root:
        return 0

    self.res = 0

    def dfs(curr,largest):
        
        if not curr:
            return None
        
        if curr.val >= largest:
            self.res += 1
            largest = curr.val
            
        dfs(curr.left, largest)
        dfs(curr.right, largest)

    dfs(root, root.val)

    return self.res