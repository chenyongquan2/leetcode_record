---
fid: "344"
title: 反转字符串
done: true
mastery: 3
---

# 344. 反转字符串

- 难度：容易　|　CodeTop 频率：24
- 链接：https://leetcode.cn/problems/reverse-string/

## 思路

首尾双指针 `lo`、`hi` 向中间靠拢，每次交换 `s[lo]` 和 `s[hi]` 后各自前进一步，直到 `lo >= hi`，即完成原地反转。（由代码自动总结，可自行修改）

## 复杂度

- 时间：O(n)
- 空间：O(1)

## 易错点 / 回顾记录

- 2026-08-31：首次完成。
