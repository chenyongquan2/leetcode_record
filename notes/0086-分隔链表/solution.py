# 86. 分隔链表
# https://leetcode.cn/problems/partition-list/
# 思路：双虚拟头节点拆成「< x」和「>= x」两条链，逐节点断链分挂，最后拼接

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        #存在小于x的节点链表
        dummy1=ListNode(-1)
        #存在大于或等于x的节点链表
        dummy2=ListNode(-1)
        #p1,p2负责两个链表的指针移动
        p1,p2=dummy1,dummy2
        #p负责遍历原链表,然后将每一个节点分别挂在p1,p2链表上
        p=head
        while p is not None:
            if p.val < x:
                p1.next=p
                p1=p1.next
            else:
                p2.next=p
                p2=p2.next

            #先记住本来p的下一个节点
            newNext=p.next
            #p得需要和本来的下一个节点进行断链
            p.next=None
            #到下一个节点
            p=newNext

        #接上两个链表
        p1.next=dummy2.next
        return dummy1.next


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
    assert to_list(s.partition(build([1, 4, 3, 2, 5, 2]), 3)) == [1, 2, 2, 4, 3, 5]
    assert to_list(s.partition(build([2, 1]), 2)) == [1, 2]
    assert to_list(s.partition(build([]), 0)) == []
    assert to_list(s.partition(build([4, 5, 6]), 3)) == [4, 5, 6]
    print("all tests passed")
