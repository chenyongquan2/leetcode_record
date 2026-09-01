---
fid: "567"
title: 字符串的排列
done: true
mastery: 3
---

# 567. 字符串的排列

- 难度：中等　|　CodeTop 频率：20
- 链接：https://leetcode.cn/problems/permutation-in-string/

## 思路

- **滑动窗口，同 [76. 最小覆盖子串](../0076-最小覆盖子串/README.md) 的模板**：`need = Counter(s1)`、`window` 计数窗口内字符、`valid` 统计已凑够数量的字符种数。
- 右指针吸收字符，`window[c] += 1` 后恰好 `window[c] == need[c]` 时 `valid += 1`；当 `valid == len(need)` 时窗口已覆盖 s1 的全部字符，进入收缩。
- 与 76 题的区别在**判定条件**：76 求最小覆盖（窗口可以更长），本题要求"恰好是排列"——即窗口内除 s1 的字符外没有多余字符。在收缩到临界点（`window[d] == need[d]`，再移就不合法）时检查 `hi - lo == len(s1)`：长度恰好相等说明窗口就是 s1 的一个排列，返回 True。
- 收缩循环里 `valid -= 1` 之后**别忘了 `window[d] -= 1`**（代码里特意标了 Todo 提醒），否则计数表和窗口内容不一致，后续判断全错。

## 复杂度

- 时间：O(|s1| + |s2|)（lo、hi 各最多走 |s2| 步）
- 空间：O(字符集大小)（need / window 两张计数表）

## 易错点 / 回顾记录

- 2026-09-01：首次完成，掌握程度 3 星。两个坑：① 只 `from collections import Counter` 却用了 `defaultdict`，漏 import 直接 NameError（录入时已补上）；② 收缩时 `valid -= 1` 后容易忘记 `window[d] -= 1`。
