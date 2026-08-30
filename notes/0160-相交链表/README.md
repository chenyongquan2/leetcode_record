---
fid: "160"
title: 相交链表
done: true
mastery: 1
---

# 160. 相交链表

- 难度：容易　|　CodeTop 频率：202
- 链接：https://leetcode.cn/problems/intersection-of-two-linked-lists/

## 思路

- 难点在于两个链表**不同长**，双指针无法步伐一致。技巧是"假装把两个链表拼起来"：`p1` 从 `headA` 走，走完接着从 `headB` 走；`p2` 从 `headB` 走，走完接着从 `headA` 走。
- 这样两个指针走的总路程都是 `lenA + lenB`，路程相同、步速相同，若相交必然同时到达交点；若不相交则同时走到 `None`（`p1 == p2 == None`），循环同样退出并返回 `None`——无需单独处理不相交的情况。
- 详细原理图见：[labuladong 单链表技巧总结](https://labuladong.online/zh/algo/essential-technique/linked-list-skills-summary/#%E5%8D%95%E9%93%BE%E8%A1%A8%E7%9A%84%E5%88%86%E8%A7%A3)

## 复杂度

- 时间：O(m + n)
- 空间：O(1)

## 易错点 / 回顾记录

- 2026-08-30：首次完成，看着题解写的。注意指针走完本链表后是切到**对方**的链表头（p1→headB、p2→headA），别写反；循环条件 `while p1 != p2` 同时覆盖了"在交点相遇"和"都走到 None"两种退出情况。
