---
fid: "26"
title: 删除排序数组中的重复项
done: true
mastery: 1
---

# 26. 删除排序数组中的重复项

- 难度：容易　|　CodeTop 频率：47
- 链接：https://leetcode.cn/problems/remove-duplicates-from-sorted-array/

## 思路

- **快慢指针原地去重**：`slow` 维护"已去重的前缀"，`fast` 在前面探路。不变量：`nums[0..slow]` 无重复。
- 数组有序，重复元素必然相邻，所以只需比较 `nums[fast] != nums[slow]`：不相等说明遇到了新元素，`slow` 先前移一格再写入 `nums[slow] = nums[fast]`。
- 返回的是**长度**，即最后一个有效索引 + 1，也就是 `slow + 1`。

## 复杂度

- 时间：O(n)
- 空间：O(1)

## 易错点 / 回顾记录

- 2026-08-31：首次完成。两个细节：遇到新元素是"先 `slow += 1` 再赋值"（顺序反了会覆盖掉 `nums[slow]` 自己）；返回值是 `slow + 1` 不是 `slow`（长度 = 索引 + 1）。空数组要单独判掉，否则 `nums[slow]` 越界。
