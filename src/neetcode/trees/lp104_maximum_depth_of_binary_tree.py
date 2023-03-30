from src.data_structures.trees import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        match root:
            case None:
                return 0
            case node:
                left = self.maxDepth(node.left)
                right = self.maxDepth(node.right)

                return 1 + max(left, right)
