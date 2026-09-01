# 543. 二叉树的直径
# https://leetcode.cn/problems/diameter-of-binary-tree/
# 思路：后序遍历求深度，在每个节点顺便用 左深+右深 更新经过该节点的最长路径（按节点数记，最后 -1 转成边数）。

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        def getDepth(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            lh=getDepth(root.left)
            rh=getDepth(root.right)
            dia=1+lh+rh
            nonlocal ans
            ans=max(ans,dia)

            return 1+max(lh,rh)
        getDepth(root)
        return ans-1


if __name__ == "__main__":
    sol = Solution()

    # [1,2,3,4,5] -> 3（路径 4-2-1-3 或 5-2-1-3）
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert sol.diameterOfBinaryTree(root) == 3

    # 单节点 -> 0
    assert sol.diameterOfBinaryTree(TreeNode(1)) == 0

    # [1,2] -> 1
    assert sol.diameterOfBinaryTree(TreeNode(1, TreeNode(2))) == 1

    # 直径不经过根：5-3-2-4-6 共 4 条边，而经过根只有 3 条
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(5)), TreeNode(4, TreeNode(6))))
    assert sol.diameterOfBinaryTree(root) == 4

    print("all tests passed")
