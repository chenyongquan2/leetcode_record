# 83. 删除排序链表中的重复元素
# https://leetcode.cn/problems/remove-duplicates-from-sorted-list/
# 思路：快慢指针，同第 26 题数组去重，把数组赋值换成指针接续，最后断开 slow 之后的重复尾巴

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #和 力扣第 26 题「删除有序数组中的重复项」 类似，唯一的区别是把数组赋值操作变成操作指针而已
        if head is None:
            return None
        fast,slow=head,head
        while fast is not None:
            if slow.val != fast.val:
                slow.next=fast
                slow=slow.next
            fast=fast.next

        #注意：断开与后面重复的元素的连接，slow一定为最后一个节点
        slow.next=None

        return head


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
    assert to_list(s.deleteDuplicates(build([1, 1, 2]))) == [1, 2]
    assert to_list(s.deleteDuplicates(build([1, 1, 2, 3, 3]))) == [1, 2, 3]
    assert s.deleteDuplicates(build([])) is None
    # 结尾全是重复元素时，验证尾巴被正确断开
    assert to_list(s.deleteDuplicates(build([1, 2, 2, 2]))) == [1, 2]
    print("all tests passed")
