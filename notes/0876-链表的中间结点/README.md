---
fid: "876"
title: 链表的中间结点
done: true
mastery: 3
---

# 876. 链表的中间结点

- 难度：容易　|　CodeTop 频率：15
- 链接：https://leetcode.cn/problems/middle-of-the-linked-list/

## 思路

- **快慢指针**：`slow`、`fast` 同时从 `head` 出发，快指针一次走两步、慢指针一次走一步。
- 循环条件 `fast is not None and fast.next is not None`——快指针走到最后一个节点或 `None`（即再也不能一次走两步）时停止，此时 `slow` 的位置就是中间节点。
- 偶数长度时该写法返回**中间两个节点中的第二个**，正符合本题要求。

## 复杂度

- 时间：O(n)，快指针扫一遍
- 空间：O(1)

## 易错点 / 回顾记录

- 2026-08-30：首次完成，很熟练。循环条件两个判断的顺序不能反：先判 `fast is not None` 再判 `fast.next`，否则空指针。
