---
fid: "83"
title: 删除排序链表中的重复元素
done: true
mastery: 2
---

# 83. 删除排序链表中的重复元素

- 难度：容易　|　CodeTop 频率：69
- 链接：https://leetcode.cn/problems/remove-duplicates-from-sorted-list/

## 思路

- 和第 26 题「[删除有序数组中的重复项](../0026-删除排序数组中的重复项/README.md)」是同一个快慢指针套路，唯一区别是把数组赋值 `nums[slow] = nums[fast]` 换成指针接续 `slow.next = fast; slow = slow.next`。
- `slow` 维护"已去重的前缀链表"，`fast` 探路；链表有序，重复必相邻，遇到 `fast.val != slow.val` 的新值就接到 `slow` 后面。
- 遍历结束后 `slow` 是去重链表的最后一个节点，**必须 `slow.next = None` 断尾**——否则 `slow` 后面还挂着原链表结尾的重复节点（如 `1→2→2→2` 会返回 `1→2→2→2`）。

## 复杂度

- 时间：O(n)
- 空间：O(1)

## 易错点 / 回顾记录

- 2026-08-31：首次完成，还行。最容易漏的是最后的 `slow.next = None` 断尾：数组版靠返回长度截断，链表版必须显式切断与后面重复节点的连接，结尾有重复时才正确。
