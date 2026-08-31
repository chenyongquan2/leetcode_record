---
fid: "27"
title: 移除元素
done: true
mastery: 1
---

# 27. 移除元素

- 难度：容易　|　CodeTop 频率：5
- 链接：https://leetcode.cn/problems/remove-element/

## 思路

- **快慢指针**：`fast` 探路，遇到 `nums[fast] != val`（要保留的元素）就压到 `nums[slow]`，然后 `slow += 1`。不变量：`nums[0..slow-1]` 是已筛选出的保留元素。
- 返回 `slow` 就是新长度（`slow` 停在有效区的下一个位置）。
- 和同族题的对照：本题是「[283. 移动零](../0283-移动零/README.md)」的第一遍（283 = 移除 0 + 尾部补 0）；与「[26. 删除排序数组中的重复项](../0026-删除排序数组中的重复项/README.md)」的区别是不变量——本题有效区是 `nums[0..slow-1]`（先赋值再 `slow += 1`），26 题有效区是 `nums[0..slow]`（先 `slow += 1` 再赋值）。

## 复杂度

- 时间：O(n)
- 空间：O(1)

## 易错点 / 回顾记录

- 2026-08-31：首次完成，看着写出来但赋值那行写错过：写成了 `nums[slow] = val`，正确的是 `nums[slow] = nums[fast]`——是把 fast 探到的**保留元素**搬过来，不是把 val 填进去。
