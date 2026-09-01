# 104. 二叉树的最大深度
# https://leetcode.cn/problems/maximum-depth-of-binary-tree/
# 思路：递归（后序）：最大深度 = 1 + max(左子树深度, 右子树深度)，空节点深度为 0。

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getDepth(root)

    def getDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        ld=self.getDepth(root.left)
        rd=self.getDepth(root.right)
        return 1+max(ld,rd)


if __name__ == "__main__":
    sol = Solution()

    # [3,9,20,null,null,15,7] -> 3
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert sol.maxDepth(root) == 3

    # [1,null,2] -> 2
    assert sol.maxDepth(TreeNode(1, None, TreeNode(2))) == 2

    # 空树 -> 0
    assert sol.maxDepth(None) == 0

    # 单节点 -> 1
    assert sol.maxDepth(TreeNode(1)) == 1

    print("all tests passed")
