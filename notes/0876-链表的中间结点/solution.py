# 876. 链表的中间结点
# https://leetcode.cn/problems/middle-of-the-linked-list/
# 思路：快慢指针，快指针一次两步、慢指针一次一步，快指针走不动时慢指针即中点

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #快慢指针，等到快指针走到最后一个节点或者None节点时，也就是快指针再也不能一次走两步时，就停止，此时slow的位置就是答案
        slow,fast=head,head
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next

        return slow


if __name__ == "__main__":
    def build(vals):
        dummy = ListNode()
        p = dummy
        for v in vals:
            p.next = ListNode(v)
            p = p.next
        return dummy.next

    def to_list(node):
        out = []
        while node is not None:
            out.append(node.val)
            node = node.next
        return out

    s = Solution()
    # 奇数长度：返回正中间的节点
    assert to_list(s.middleNode(build([1, 2, 3, 4, 5]))) == [3, 4, 5]
    # 偶数长度：返回中间两个节点中的第二个
    assert to_list(s.middleNode(build([1, 2, 3, 4, 5, 6]))) == [4, 5, 6]
    assert to_list(s.middleNode(build([1]))) == [1]
    print("all tests passed")
