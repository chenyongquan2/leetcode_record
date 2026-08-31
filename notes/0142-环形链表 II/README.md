---
fid: "142"
title: 环形链表 II
done: true
mastery: 3
---

# 142. 环形链表 II

- 难度：中等　|　CodeTop 频率：170
- 链接：https://leetcode.cn/problems/linked-list-cycle-ii/

## 思路

- **第一阶段判环**：快慢指针（快 2 步、慢 1 步），相遇则有环；`fast` 或 `fast.next` 变成 `None` 则无环，返回 `None`。
- **第二阶段找入环点**：相遇后把 `slow` 拉回 `head`，两个指针改为**同速**（各走 1 步）前进，再次相遇的位置就是入环点。
- 原理：相遇时 `fast` 走的步数是 `slow` 的 2 倍，设 `slow` 走了 k 步，则 `fast` 多走的 k 步全是在环里绕圈；设相遇点距入环点为 m，则 head 到入环点距离 = k - m，相遇点再走 k - m 步也恰好回到入环点——所以同速走必在入环点相遇。
- 原理图见：[labuladong 单链表技巧总结](https://labuladong.online/zh/algo/essential-technique/linked-list-skills-summary/#%E5%8D%95%E9%93%BE%E8%A1%A8%E7%9A%84%E5%88%86%E8%A7%A3)

## 复杂度

- 时间：O(n)
- 空间：O(1)

## 易错点 / 回顾记录

- 2026-08-30：首次完成，还行。注意 break 出循环后要再判一次 `fast is None or fast.next is None` 区分"相遇"和"走到头"两种退出方式，不能直接进第二阶段。
