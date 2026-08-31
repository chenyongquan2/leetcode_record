# 易错知识点汇总

从各题笔记的「`## 知识点：…`」小节自动汇总，用于集中复习。
内容请在对应题目的笔记里修改，然后运行 `python scripts/gen_readme.py` 重新生成本页。

**共 2 条，来自 1 道题**　（更新于 2026-08-31）

## 23. 合并K个排序链表

### `if head is not None:` 与 `if head:` 是否等价

- `if head:` 判断的是对象**真值**（truthiness）：`None`/`False`/`0`/空容器为假；类定义了 `__bool__` 或 `__len__` 则按其返回值；否则普通对象实例一律为真。
- `ListNode` 没定义 `__bool__`/`__len__`，所以任何节点实例都是真（哪怕 `val` 是 0），只有 `None` 被判假——**在链表节点场景两种写法等价**，`node.next is not None` 同理可简写为 `node.next`。
- 但若变量可能是数字/字符串/容器就不等价了：如 `if node.val:` 遇到 `val=0` 会被误判为假，是真实的坑。
- PEP 8 建议：想表达"不是 None"时显式写 `is not None`，更严谨。

### `while pq:` 不能写成 `while pq is not None:`

- `pq` 是**列表**，从头到尾都是同一个 list 对象，`heappop` 弹空后是 `[]` 而不是 `None`，所以 `pq is not None` 永远为真 → 空堆继续 pop 会抛 `IndexError`（相当于死循环条件）。
- `while pq:` 判断的是真值：list 定义了 `__len__`，空列表为假、非空为真，含义是"堆非空就继续"，等价于 `while len(pq) > 0:`，这才是正确的循环条件。
- 两条规则合起来记：
  - 判断**链表节点**存不存在 → `is not None` 与真值判断等价（节点对象永远为真），写 `is not None` 更严谨。
  - 判断**容器（list/dict/str）空不空** → 必须用真值判断（`while pq:` 或 `len(pq) > 0`），**不能**用 `is not None`，因为空容器 ≠ None。
- 一句话：`is not None` 问的是"这个东西**在不在**"，真值判断问的是"这个东西**空不空**"——对节点两个问题答案恰好相同，对容器则完全是两回事。

> 出处：[23. 合并K个排序链表 的笔记](notes/0023-%E5%90%88%E5%B9%B6K%E4%B8%AA%E6%8E%92%E5%BA%8F%E9%93%BE%E8%A1%A8/README.md)
