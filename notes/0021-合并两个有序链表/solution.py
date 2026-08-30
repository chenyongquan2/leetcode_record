# 21. 合并两个有序链表
# https://leetcode.cn/problems/merge-two-sorted-lists/
# 思路：虚拟头节点 + 双指针，每轮把较小的节点接到结果链表尾部，最后接上剩余部分

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #虚拟头节点
        dummy = ListNode(-1)
        p=dummy
        p1=list1
        p2=list2
        while p1 is not None and p2 is not None:
            #比较p1和p2,把较小的节点接到p指针
            if p1.val > p2.val:
                p.next=p2
                p2=p2.next
            else:
                p.next=p1
                p1=p1.next
            #p指针不断往前移
            p=p.next

        #接上剩余的节点
        if p1 is not None:
            p.next=p1
        if p2 is not None:
            p.next=p2

        return dummy.next


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
    assert to_list(s.mergeTwoLists(build([1, 2, 4]), build([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert to_list(s.mergeTwoLists(build([]), build([]))) == []
    assert to_list(s.mergeTwoLists(build([]), build([0]))) == [0]
    print("all tests passed")
