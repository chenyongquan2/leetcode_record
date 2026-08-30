# 19. 删除链表的倒数第N个节点
# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
# 思路：虚拟头节点 + 快慢指针，先找到倒数第 n+1 个节点，再把它的 next 跳过一个

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #要删除倒数第n个节点，得先找到倒数第n+1个节点
        #技巧:为了防止出现空指针的情况，比如链表总共5个节点，要你删除倒数第5个节点，那么就是顺数第1个节点
        #那么首先要找倒数第6个节点，但是第一个节点前面已经没节点了，所以我们才要加一个dummy虚拟节点，这种情况就能正常删除了
        dummy=ListNode(val=-1,next=head)
        #注意：找倒数第n个节点，即使前面加了新的节点也没有关系
        x=self.findNthFromEnd(dummy,n+1)
        x.next=x.next.next
        return dummy.next

    def findNthFromEnd(self,head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #快指针比慢指针先走n步，然后再一起走，这样当快指针到达末尾None位置时，慢指针的位置就是第n个
        fast=head
        for i in range(n):
            fast=fast.next
        slow=head
        while fast is not None:
            fast=fast.next
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
    assert to_list(s.removeNthFromEnd(build([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
    assert to_list(s.removeNthFromEnd(build([1]), 1)) == []
    assert to_list(s.removeNthFromEnd(build([1, 2]), 1)) == [1]
    assert to_list(s.removeNthFromEnd(build([1, 2]), 2)) == [2]
    print("all tests passed")
