def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
    if not root:
        return True

    def findHeight(root):
        if not root:
            return 0

        return 1 + max(findHeight(root.left), findHeight(root.right))

    lheight = findHeight(root.left)
    rheight = findHeight(root.right)

    if abs(lheight - rheight) > 1:
        return False
    else:
        return self.isBalanced(root.left) and self.isBalanced(root.right)