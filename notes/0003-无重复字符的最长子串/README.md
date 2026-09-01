---
fid: "3"
title: 无重复字符的最长子串
done: true
mastery: 1
---

# 3. 无重复字符的最长子串

- 难度：中等　|　CodeTop 频率：1190（全表第 1）
- 链接：https://leetcode.cn/problems/longest-substring-without-repeating-characters/

## 思路

- **滑动窗口，是这一族（[76](../0076-最小覆盖子串/README.md)/[567](../0567-字符串的排列/README.md)/[438](../0438-找到字符串中所有字母异位词/README.md)）里最简单的形态**：不需要 need 表和 valid 计数，只用一张 `window` 计数表。
- 右指针吸收字符 `c` 后，若 `window[c] > 1` 说明窗口里出现了重复，收缩左端：不断移出 `s[lo]` 直到把前一个 `c` 挤出窗口（循环条件恰好是 `window[c] > 1`）。
- 收缩循环结束后窗口内保证无重复，此时用 `hi - lo` 更新答案。注意本题在**收缩之后**更新答案（要窗口合法时算长度），和 76 在收缩中的临界点更新不同。

## 复杂度

- 时间：O(n)（lo、hi 各最多走 n 步）
- 空间：O(字符集大小)（window 计数表）

## 知识点：defaultdict 的 key 写错不会报错，只会静默插入

滑动窗口收缩时取"即将移出的字符"必须写 `d = s[lo]`（从字符串取字符），写成 `d = window[lo]` 是拿下标去查字符计数表。普通 dict 会立刻 `KeyError` 暴露问题，但 `defaultdict(int)` 会**静默返回 0 并把错误的 key 插进表里**，后果是真正重复字符的计数永远减不下去，`while window[c] > 1` 直接死循环。调这类 bug 可以临时把 defaultdict 换成普通 dict 让它炸出来。

## 易错点 / 回顾记录

- 2026-09-01：首次完成，掌握程度 1 星。第一版把 `d = s[lo]` 写成了 `d = window[lo]`，在 `"abba"` 这类有重复的输入上死循环；defaultdict 静默吞掉了错误 key（见知识点）。
