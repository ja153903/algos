from src.data_structures.trees import TreeNode


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root
