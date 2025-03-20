def isValidBST(self, root: Optional[TreeNode]) -> bool:

    def helper(node, leftBound, rightBound):

        if not node:
            return True

        if not (leftBound < node.val < rightBound):
            return False

        return helper(node.left, leftBound, node.val) and helper(node.right, node.val, rightBound)

    
    return helper(root, float('-inf'), float('inf'))