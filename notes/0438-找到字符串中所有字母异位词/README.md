---
fid: "438"
title: 找到字符串中所有字母异位词
done: true
mastery: 2
---

# 438. 找到字符串中所有字母异位词

- 难度：中等　|　CodeTop 频率：15
- 链接：https://leetcode.cn/problems/find-all-anagrams-in-a-string/

## 思路

- **滑动窗口，与 [76](../0076-最小覆盖子串/README.md)、[567](../0567-字符串的排列/README.md) 同一套模板**：`need = Counter(p)`、`window` 计数、`valid` 统计凑够数量的字符种数。
- 本题就是 567（判断是否存在排列）的"收集所有解"版本：567 找到一个就 `return True`，这里改成 `res.append(lo)` 把每个异位词的起始下标都记下来，窗口继续滑。
- 判定条件同样在收缩临界点（`window[d] == need[d]`，`valid` 即将减一）检查 `hi - lo == len(p)`：长度恰好相等才是异位词。反例 `s="cbba", p="abc"`——窗口 `"cbba"` 虽然 valid 满了，但多出一个 `b`，长度 4 ≠ 3，不能记入答案。
- 记录的是**左端点 `lo`**，且要在 `lo += 1` 之前记录。

## 复杂度

- 时间：O(|s| + |p|)（lo、hi 各最多走 |s| 步）
- 空间：O(字符集大小)（need / window 两张计数表，res 不计）

## 易错点 / 回顾记录

- 2026-09-01：首次完成，掌握程度 2 星。易错点：① 必须验证 `hi - lo == len(p)` 才能记答案（valid 满 ≠ 是异位词，可能混入多余字符）；② 用了 `List[int]` 注解但漏了 `from typing import List`（录入时已补上）。
