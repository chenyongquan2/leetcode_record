---
fid: "23"
title: 合并K个排序链表
done: true
mastery: 1
---

# 23. 合并K个排序链表

- 难度：困难　|　CodeTop 频率：259
- 链接：https://leetcode.cn/problems/merge-k-sorted-lists/

## 思路

最小堆（优先级队列）解法：

1. 建虚拟头节点 `dummy`，`p` 指针负责拼接结果链表。
2. 把 k 个链表的头节点以 `(val, i, node)` 元组形式全部压入最小堆——`i` 是链表下标，当 `val` 相同时作为 tie-breaker，避免 Python 去比较两个 `ListNode` 对象而报错。
3. 每次弹出堆顶（当前 k 路中最小的节点）接到 `p.next`，若该节点还有后继，就把后继补入堆中。
4. 堆空时结束，返回 `dummy.next`。

## 复杂度

- 时间：O(N log k)，N 为所有节点总数，k 为链表条数，每个节点进出堆各一次
- 空间：O(k)，堆中最多同时存 k 个节点

## 知识点：`if head is not None:` 与 `if head:` 是否等价

- `if head:` 判断的是对象**真值**（truthiness）：`None`/`False`/`0`/空容器为假；类定义了 `__bool__` 或 `__len__` 则按其返回值；否则普通对象实例一律为真。
- `ListNode` 没定义 `__bool__`/`__len__`，所以任何节点实例都是真（哪怕 `val` 是 0），只有 `None` 被判假——**在链表节点场景两种写法等价**，`node.next is not None` 同理可简写为 `node.next`。
- 但若变量可能是数字/字符串/容器就不等价了：如 `if node.val:` 遇到 `val=0` 会被误判为假，是真实的坑。
- PEP 8 建议：想表达"不是 None"时显式写 `is not None`，更严谨。

## 知识点：`while pq:` 不能写成 `while pq is not None:`

- `pq` 是**列表**，从头到尾都是同一个 list 对象，`heappop` 弹空后是 `[]` 而不是 `None`，所以 `pq is not None` 永远为真 → 空堆继续 pop 会抛 `IndexError`（相当于死循环条件）。
- `while pq:` 判断的是真值：list 定义了 `__len__`，空列表为假、非空为真，含义是"堆非空就继续"，等价于 `while len(pq) > 0:`，这才是正确的循环条件。
- 两条规则合起来记：
  - 判断**链表节点**存不存在 → `is not None` 与真值判断等价（节点对象永远为真），写 `is not None` 更严谨。
  - 判断**容器（list/dict/str）空不空** → 必须用真值判断（`while pq:` 或 `len(pq) > 0`），**不能**用 `is not None`，因为空容器 ≠ None。
- 一句话：`is not None` 问的是"这个东西**在不在**"，真值判断问的是"这个东西**空不空**"——对节点两个问题答案恰好相同，对容器则完全是两回事。

## 易错点 / 回顾记录

- 2026-08-30：首次完成。堆中元素用 `(val, i, node)` 加下标做 tie-breaker 是关键；顺带整理了 `if head is not None` vs `if head` 的真值判断知识点（见上）。
- 2026-08-30：补充知识点：`while pq:` 不能写成 `while pq is not None:`（容器判空必须用真值判断，见上）。
