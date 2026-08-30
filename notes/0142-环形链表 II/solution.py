# 142. 环形链表 II
# https://leetcode.cn/problems/linked-list-cycle-ii/
# 思路：快慢指针相遇后，把 slow 拉回 head，两指针同速再走，再次相遇处即入环点

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast=head,head
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next
            if fast == slow:
                break

        #fast遇到空指针，则说明没有还
        if fast is None or fast.next is None:
            return None

        # 原理图见: https://labuladong.online/zh/algo/essential-technique/linked-list-skills-summary/#%E5%8D%95%E9%93%BE%E8%A1%A8%E7%9A%84%E5%88%86%E8%A7%A3

        slow=head
        while slow != fast:
            fast=fast.next
            slow=slow.next

        return slow


if __name__ == "__main__":
    def build(vals, pos):
        """按 vals 建链表，尾节点指向下标 pos 的节点成环（pos=-1 不成环）。返回 (head, 节点列表)。"""
        nodes = [ListNode(v) for v in vals]
        for a, b in zip(nodes, nodes[1:]):
            a.next = b
        if nodes and pos >= 0:
            nodes[-1].next = nodes[pos]
        return (nodes[0] if nodes else None), nodes

    s = Solution()
    head, nodes = build([3, 2, 0, -4], 1)
    assert s.detectCycle(head) is nodes[1]
    head, nodes = build([1, 2], 0)
    assert s.detectCycle(head) is nodes[0]
    head, _ = build([1], -1)
    assert s.detectCycle(head) is None
    assert s.detectCycle(None) is None
    print("all tests passed")
