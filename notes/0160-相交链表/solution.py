# 160. 相交链表
# https://leetcode.cn/problems/intersection-of-two-linked-lists/
# 思路：双指针各自走完本链表后换到对方链表头继续走，两指针路程相同，必在交点（或 None）相遇

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #详细思路见：https://labuladong.online/zh/algo/essential-technique/linked-list-skills-summary/#%E5%8D%95%E9%93%BE%E8%A1%A8%E7%9A%84%E5%88%86%E8%A7%A3
        #这题的难点时两个链表不同长，那么无法步伐一致，那么我们可以假装把两个链表拼起来
        #p1这个走完，从headB继续走；p2这个链表走完，从headA开始继续走
        p1,p2=headA,headB
        #如果没有交集，那么最终p1=p2=None
        while p1 != p2:
            if p1 is None:
                p1=headB
            else:
                p1=p1.next

            if p2 is None:
                p2=headA
            else:
                p2=p2.next

        return p1


if __name__ == "__main__":
    def build(vals):
        nodes = [ListNode(v) for v in vals]
        for a, b in zip(nodes, nodes[1:]):
            a.next = b
        return nodes

    s = Solution()
    # 示例 1：A = [4,1,8,4,5]，B = [5,6,1,8,4,5]，在值为 8 的节点相交
    common = build([8, 4, 5])
    a = build([4, 1])
    a[-1].next = common[0]
    b = build([5, 6, 1])
    b[-1].next = common[0]
    assert s.getIntersectionNode(a[0], b[0]) is common[0]
    # 不相交
    x = build([2, 6, 4])
    y = build([1, 5])
    assert s.getIntersectionNode(x[0], y[0]) is None
    # 完全重合（交点即两链表头）
    z = build([1, 2, 3])
    assert s.getIntersectionNode(z[0], z[0]) is z[0]
    print("all tests passed")
