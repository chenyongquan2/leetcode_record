# 144. 二叉树的前序遍历
# https://leetcode.cn/problems/binary-tree-preorder-traversal/
# 思路：递归遍历，进入节点时先记录 root.val（前序位置），再递归左、右子树。

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]

        def travel(root: Optional[TreeNode]):
            if root is None:
                return
            res.append(root.val)
            travel(root.left)
            travel(root.right)

        travel(root)
        return res


if __name__ == "__main__":
    sol = Solution()

    # [1,null,2,3] -> [1,2,3]
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert sol.preorderTraversal(root) == [1, 2, 3]

    # 空树 -> []
    assert sol.preorderTraversal(None) == []

    # 单节点 -> [1]
    assert sol.preorderTraversal(TreeNode(1)) == [1]

    # [3,9,20,null,null,15,7] -> [3,9,20,15,7]
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert sol.preorderTraversal(root) == [3, 9, 20, 15, 7]

    print("all tests passed")
