def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    
    self.res = []

    def dfs(node, currsum, k, temp):

        if not node:
            return None

        currsum += node.val
        temp.append(node.val)

        if not node.left and not node.right and currsum == k:
            self.res.append(list(temp))

            
        dfs(node.left, currsum, k, temp)
        dfs(node.right, currsum, k, temp)


        temp.pop()

    dfs(root, 0, targetSum, [])
    return self.res