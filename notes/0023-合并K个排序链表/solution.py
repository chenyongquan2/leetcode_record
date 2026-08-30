# 23. 合并K个排序链表
# https://leetcode.cn/problems/merge-k-sorted-lists/
# 思路：最小堆，k 个链表头先入堆，每次弹出最小节点接到结果链表，再把它的 next 补入堆

import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        #虚拟头节点
        dummy=ListNode(-1)
        p=dummy

        #优先级队列，默认就是最小堆(堆顶是最小的)
        pq=[]

        #将k个链表的头节点放到最小堆
        for i,head in enumerate(lists):
            # 【知识点】if head is not None: 与 if head: 在这里等价：
            # if head 判断的是"真值"，ListNode 没定义 __bool__/__len__，
            # 普通对象实例一律为真（哪怕 head.val 是 0），所以只有 None 会被判假。
            # 但两者语义不同：若变量可能是数字/字符串/容器（如 if node.val:），
            # 遇到 0、""、[] 会被误判为假。想表达"不是 None"时，
            # PEP 8 推荐显式写 is not None，更严谨。
            if head is not None:
                #当head.val相同时，用元组的下一个属性i作为tie-breaker去打破比较的平衡
                item=(head.val,i,head)
                heapq.heappush(pq,item)

        #每次从最小堆里面取出来一个最小的元素，拼接到链表上
        while pq:
            val,i,node = heapq.heappop(pq)
            p.next=node

            #p不断前进
            p=p.next

            #第k个链表的下一个元素替代node进入最小堆
            if node.next is not None:
                item=(node.next.val,i,node.next)
                heapq.heappush(pq, item)

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
    assert to_list(s.mergeKLists([build([1, 4, 5]), build([1, 3, 4]), build([2, 6])])) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert to_list(s.mergeKLists([])) == []
    assert to_list(s.mergeKLists([build([])])) == []
    print("all tests passed")
