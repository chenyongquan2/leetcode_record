# LeetCode 刷题笔记

按 [CodeTop](https://codetop.cc/home) 面试频率排序的刷题记录。每道题一个文件夹（`notes/题号-题名/`），
包含笔记 `README.md` 和 `solution.py` / `solution.cpp` 两种语言的题解。

**进度：12 / 1155**　（数据更新于 2026-08-31，完整列表见 [PROBLEMS.md](PROBLEMS.md)，易错知识点汇总见 [TIPS.md](TIPS.md)）

## 使用方法

**方式一（推荐）：** 直接把「题号 + 题解代码（Python/C++）+ 思路（可选）」发给 Claude Code，
它会按项目 skill [record-note](.claude/skills/record-note/SKILL.md) 自动录入笔记、刷新表格并提交。

**方式二：手动操作**

```bash
# 刷完一道题后，新建这道题的笔记（按题号，如 3、146、"剑指Offer22"、"补充题4"）
python scripts/new_note.py 3

# 在 notes/0003-无重复字符的最长子串/ 里写笔记和题解，
# 并在其 README.md 顶部 frontmatter 中维护 done（是否完成）和 mastery（掌握程度 0-3）

# 重新生成本页和 PROBLEMS.md 的表格
python scripts/gen_readme.py

# 更新 CodeTop 频率数据（可选：设置 CODETOP_COOKIE 环境变量可同步你在 codetop 上的完成/掌握状态）
python scripts/fetch_codetop.py && python scripts/gen_readme.py
```

## 高频 Top 100

| # | 题目 | 难度 | 频率 | 最近考察 | 完成 | 掌握 | 笔记 | 题解 |
|---:|---|---|---:|---|:---:|---|---|---|
| 1 | [3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) | 中等 | 1190 | 2026-08-29 |  |  |  |  |
| 2 | [146. LRU缓存机制](https://leetcode.cn/problems/lru-cache/) | 中等 | 952 | 2026-08-28 |  |  |  |  |
| 3 | [206. 反转链表](https://leetcode.cn/problems/reverse-linked-list/) | 容易 | 750 | 2026-08-09 |  |  |  |  |
| 4 | [215. 数组中的第K个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/) | 中等 | 602 | 2026-08-26 |  |  |  |  |
| 5 | [25. K 个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group/) | 困难 | 529 | 2026-08-28 |  |  |  |  |
| 6 | [15. 三数之和](https://leetcode.cn/problems/3sum/) | 中等 | 489 | 2026-08-26 |  |  |  |  |
| 7 | [53. 最大子数组和](https://leetcode.cn/problems/maximum-subarray/) | 中等 | 375 | 2026-07-16 |  |  |  |  |
| 8 | [补充题4. 手撕快速排序](https://leetcode.cn/problems/sort-an-array/) | 中等 | 357 | 2026-08-16 |  |  |  |  |
| 9 | [5. 最长回文子串](https://leetcode.cn/problems/longest-palindromic-substring/) | 中等 | 356 | 2026-08-24 |  |  |  |  |
| 10 | [21. 合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/) | 容易 | 333 | 2026-08-19 | ✅ | ★☆☆ | [笔记](notes/0021-%E5%90%88%E5%B9%B6%E4%B8%A4%E4%B8%AA%E6%9C%89%E5%BA%8F%E9%93%BE%E8%A1%A8/README.md) | [Python](notes/0021-%E5%90%88%E5%B9%B6%E4%B8%A4%E4%B8%AA%E6%9C%89%E5%BA%8F%E9%93%BE%E8%A1%A8/solution.py) |
| 11 | [200. 岛屿数量](https://leetcode.cn/problems/number-of-islands/) | 中等 | 331 | 2026-08-26 |  |  |  |  |
| 12 | [102. 二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/) | 中等 | 331 | 2026-08-20 |  |  |  |  |
| 13 | [33. 搜索旋转排序数组](https://leetcode.cn/problems/search-in-rotated-sorted-array/) | 中等 | 315 | 2026-08-21 |  |  |  |  |
| 14 | [1. 两数之和](https://leetcode.cn/problems/two-sum/) | 容易 | 305 | 2026-08-03 |  |  |  |  |
| 15 | [88. 合并两个有序数组](https://leetcode.cn/problems/merge-sorted-array/) | 容易 | 299 | 2026-08-26 |  |  |  |  |
| 16 | [46. 全排列](https://leetcode.cn/problems/permutations/) | 中等 | 299 | 2026-08-11 |  |  |  |  |
| 17 | [20. 有效的括号](https://leetcode.cn/problems/valid-parentheses/) | 容易 | 297 | 2026-07-02 |  |  |  |  |
| 18 | [121. 买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/) | 容易 | 280 | 2026-07-14 |  |  |  |  |
| 19 | [300. 最长上升子序列](https://leetcode.cn/problems/longest-increasing-subsequence/) | 中等 | 273 | 2026-08-22 |  |  |  |  |
| 20 | [92. 反转链表 II](https://leetcode.cn/problems/reverse-linked-list-ii/) | 中等 | 271 | 2026-06-30 |  |  |  |  |
| 21 | [103. 二叉树的锯齿形层次遍历](https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/) | 中等 | 270 | 2026-08-22 |  |  |  |  |
| 22 | [236. 二叉树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/) | 中等 | 267 | 2026-07-06 |  |  |  |  |
| 23 | [23. 合并K个排序链表](https://leetcode.cn/problems/merge-k-sorted-lists/) | 困难 | 259 | 2026-08-21 | ✅ | ★☆☆ | [笔记](notes/0023-%E5%90%88%E5%B9%B6K%E4%B8%AA%E6%8E%92%E5%BA%8F%E9%93%BE%E8%A1%A8/README.md) | [Python](notes/0023-%E5%90%88%E5%B9%B6K%E4%B8%AA%E6%8E%92%E5%BA%8F%E9%93%BE%E8%A1%A8/solution.py) |
| 24 | [54. 螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/) | 中等 | 256 | 2026-07-30 |  |  |  |  |
| 25 | [143. 重排链表](https://leetcode.cn/problems/reorder-list/) | 中等 | 254 | 2026-08-27 |  |  |  |  |
| 26 | [141. 环形链表](https://leetcode.cn/problems/linked-list-cycle/) | 容易 | 254 | 2026-08-17 |  |  |  |  |
| 27 | [56. 合并区间](https://leetcode.cn/problems/merge-intervals/) | 中等 | 247 | 2026-08-24 |  |  |  |  |
| 28 | [415. 字符串相加](https://leetcode.cn/problems/add-strings/) | 容易 | 243 | 2026-08-20 |  |  |  |  |
| 29 | [72. 编辑距离](https://leetcode.cn/problems/edit-distance/) | 困难 | 205 | 2026-08-12 |  |  |  |  |
| 30 | [160. 相交链表](https://leetcode.cn/problems/intersection-of-two-linked-lists/) | 容易 | 202 | 2026-06-29 | ✅ | ★☆☆ | [笔记](notes/0160-%E7%9B%B8%E4%BA%A4%E9%93%BE%E8%A1%A8/README.md) | [Python](notes/0160-%E7%9B%B8%E4%BA%A4%E9%93%BE%E8%A1%A8/solution.py) |
| 31 | [42. 接雨水](https://leetcode.cn/problems/trapping-rain-water/) | 困难 | 199 | 2026-08-05 |  |  |  |  |
| 32 | [1143. 最长公共子序列](https://leetcode.cn/problems/longest-common-subsequence/) | 中等 | 198 | 2026-08-19 |  |  |  |  |
| 33 | [82. 删除排序链表中的重复元素 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/) | 中等 | 187 | 2026-08-05 |  |  |  |  |
| 34 | [124. 二叉树中的最大路径和](https://leetcode.cn/problems/binary-tree-maximum-path-sum/) | 困难 | 185 | 2026-08-06 |  |  |  |  |
| 35 | [93. 复原IP地址](https://leetcode.cn/problems/restore-ip-addresses/) | 中等 | 185 | 2026-05-12 |  |  |  |  |
| 36 | [19. 删除链表的倒数第N个节点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/) | 中等 | 184 | 2026-07-23 | ✅ | ★☆☆ | [笔记](notes/0019-%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E7%9A%84%E5%80%92%E6%95%B0%E7%AC%ACN%E4%B8%AA%E8%8A%82%E7%82%B9/README.md) | [Python](notes/0019-%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E7%9A%84%E5%80%92%E6%95%B0%E7%AC%ACN%E4%B8%AA%E8%8A%82%E7%82%B9/solution.py) |
| 37 | [4. 寻找两个正序数组的中位数](https://leetcode.cn/problems/median-of-two-sorted-arrays/) | 困难 | 174 | 2026-08-10 |  |  |  |  |
| 38 | [142. 环形链表 II](https://leetcode.cn/problems/linked-list-cycle-ii/) | 中等 | 170 | 2026-05-08 | ✅ | ★★☆ | [笔记](notes/0142-%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8%20II/README.md) | [Python](notes/0142-%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8%20II/solution.py) |
| 39 | [165. 比较版本号](https://leetcode.cn/problems/compare-version-numbers/) | 中等 | 166 | 2026-08-18 |  |  |  |  |
| 40 | [199. 二叉树的右视图](https://leetcode.cn/problems/binary-tree-right-side-view/) | 中等 | 161 | 2026-05-28 |  |  |  |  |
| 41 | [704. 二分查找](https://leetcode.cn/problems/binary-search/) | 容易 | 153 | 2026-07-29 |  |  |  |  |
| 42 | [239. 滑动窗口最大值](https://leetcode.cn/problems/sliding-window-maximum/) | 困难 | 153 | 2026-06-18 |  |  |  |  |
| 43 | [22. 括号生成](https://leetcode.cn/problems/generate-parentheses/) | 中等 | 151 | 2026-06-27 |  |  |  |  |
| 44 | [32. 最长有效括号](https://leetcode.cn/problems/longest-valid-parentheses/) | 困难 | 148 | 2026-06-04 |  |  |  |  |
| 45 | [69. x 的平方根](https://leetcode.cn/problems/sqrtx/) | 容易 | 147 | 2026-06-30 |  |  |  |  |
| 46 | [148. 排序链表](https://leetcode.cn/problems/sort-list/) | 中等 | 147 | 2026-06-07 |  |  |  |  |
| 47 | [94. 二叉树的中序遍历](https://leetcode.cn/problems/binary-tree-inorder-traversal/) | 容易 | 144 | 2026-05-20 |  |  |  |  |
| 48 | [232. 用栈实现队列](https://leetcode.cn/problems/implement-queue-using-stacks/) | 容易 | 143 | 2026-03-08 |  |  |  |  |
| 49 | [31. 下一个排列](https://leetcode.cn/problems/next-permutation/) | 中等 | 137 | 2026-08-04 |  |  |  |  |
| 50 | [76. 最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/) | 困难 | 135 | 2026-08-18 |  |  |  |  |
| 51 | [8. 字符串转换整数 (atoi)](https://leetcode.cn/problems/string-to-integer-atoi/) | 中等 | 134 | 2026-08-24 |  |  |  |  |
| 52 | [2. 两数相加](https://leetcode.cn/problems/add-two-numbers/) | 中等 | 133 | 2026-04-16 |  |  |  |  |
| 53 | [43. 字符串相乘](https://leetcode.cn/problems/multiply-strings/) | 中等 | 132 | 2026-08-27 |  |  |  |  |
| 54 | [322. 零钱兑换](https://leetcode.cn/problems/coin-change/) | 中等 | 132 | 2026-04-15 |  |  |  |  |
| 55 | [70. 爬楼梯](https://leetcode.cn/problems/climbing-stairs/) | 容易 | 131 | 2026-08-27 |  |  |  |  |
| 56 | [105. 从前序与中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | 中等 | 117 | 2026-06-29 |  |  |  |  |
| 57 | [41. 缺失的第一个正数](https://leetcode.cn/problems/first-missing-positive/) | 困难 | 114 | 2026-06-16 |  |  |  |  |
| 58 | [78. 子集](https://leetcode.cn/problems/subsets/) | 中等 | 108 | 2026-08-26 |  |  |  |  |
| 59 | [151. 翻转字符串里的单词](https://leetcode.cn/problems/reverse-words-in-a-string/) | 中等 | 106 | 2026-07-21 |  |  |  |  |
| 60 | [剑指 Offer 22. 链表中倒数第k个节点](https://leetcode.cn/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/) | 容易 | 103 | 2026-08-04 |  |  |  |  |
| 61 | [34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/) | 中等 | 103 | 2026-07-23 |  |  |  |  |
| 62 | [394. 字符串解码](https://leetcode.cn/problems/decode-string/) | 中等 | 101 | 2026-08-20 |  |  |  |  |
| 63 | [129. 求根到叶子节点数字之和](https://leetcode.cn/problems/sum-root-to-leaf-numbers/) | 中等 | 100 | 2026-04-21 |  |  |  |  |
| 64 | [155. 最小栈](https://leetcode.cn/problems/min-stack/) | 容易 | 99 | 2026-04-13 |  |  |  |  |
| 65 | [101. 对称二叉树](https://leetcode.cn/problems/symmetric-tree/) | 容易 | 97 | 2026-07-12 |  |  |  |  |
| 66 | [64. 最小路径和](https://leetcode.cn/problems/minimum-path-sum/) | 中等 | 96 | 2026-08-16 |  |  |  |  |
| 67 | [470. 用 Rand7() 实现 Rand10()](https://leetcode.cn/problems/implement-rand10-using-rand7/) | 中等 | 96 | 2026-07-21 |  |  |  |  |
| 68 | [39. 组合总和](https://leetcode.cn/problems/combination-sum/) | 中等 | 96 | 2026-05-26 |  |  |  |  |
| 69 | [695. 岛屿的最大面积](https://leetcode.cn/problems/max-area-of-island/) | 中等 | 94 | 2026-06-23 |  |  |  |  |
| 70 | [128. 最长连续序列](https://leetcode.cn/problems/longest-consecutive-sequence/) | 中等 | 93 | 2026-06-30 |  |  |  |  |
| 71 | [122. 买卖股票的最佳时机 II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/) | 容易 | 91 | 2026-06-04 |  |  |  |  |
| 72 | [104. 二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/) | 容易 | 91 | 2026-05-07 |  |  |  |  |
| 73 | [110. 平衡二叉树](https://leetcode.cn/problems/balanced-binary-tree/) | 容易 | 88 | 2026-08-06 |  |  |  |  |
| 74 | [221. 最大正方形](https://leetcode.cn/problems/maximal-square/) | 中等 | 88 | 2026-04-17 |  |  |  |  |
| 75 | [234. 回文链表](https://leetcode.cn/problems/palindrome-linked-list/) | 容易 | 86 | 2026-05-21 |  |  |  |  |
| 76 | [48. 旋转图像](https://leetcode.cn/problems/rotate-image/) | 中等 | 85 | 2026-08-19 |  |  |  |  |
| 77 | [240. 搜索二维矩阵 II](https://leetcode.cn/problems/search-a-2d-matrix-ii/) | 中等 | 85 | 2026-07-21 |  |  |  |  |
| 78 | [152. 乘积最大子数组](https://leetcode.cn/problems/maximum-product-subarray/) | 中等 | 85 | 2026-05-27 |  |  |  |  |
| 79 | [179. 最大数](https://leetcode.cn/problems/largest-number/) | 中等 | 84 | 2026-08-05 |  |  |  |  |
| 80 | [662. 二叉树最大宽度](https://leetcode.cn/problems/maximum-width-of-binary-tree/) | 中等 | 84 | 2026-07-17 |  |  |  |  |
| 81 | [14. 最长公共前缀](https://leetcode.cn/problems/longest-common-prefix/) | 容易 | 84 | 2026-06-11 |  |  |  |  |
| 82 | [98. 验证二叉搜索树](https://leetcode.cn/problems/validate-binary-search-tree/) | 中等 | 84 | 2026-04-20 |  |  |  |  |
| 83 | [144. 二叉树的前序遍历](https://leetcode.cn/problems/binary-tree-preorder-traversal/) | 容易 | 84 | 2025-04-17 |  |  |  |  |
| 84 | [543. 二叉树的直径](https://leetcode.cn/problems/diameter-of-binary-tree/) | 容易 | 82 | 2026-08-03 |  |  |  |  |
| 85 | [560. 和为K的子数组](https://leetcode.cn/problems/subarray-sum-equals-k/) | 中等 | 80 | 2026-08-17 |  |  |  |  |
| 86 | [162. 寻找峰值](https://leetcode.cn/problems/find-peak-element/) | 中等 | 80 | 2026-04-19 |  |  |  |  |
| 87 | [113. 路径总和 II](https://leetcode.cn/problems/path-sum-ii/) | 中等 | 78 | 2026-07-24 |  |  |  |  |
| 88 | [62. 不同路径](https://leetcode.cn/problems/unique-paths/) | 中等 | 78 | 2026-06-01 |  |  |  |  |
| 89 | [198. 打家劫舍](https://leetcode.cn/problems/house-robber/) | 中等 | 75 | 2026-07-28 |  |  |  |  |
| 90 | [209. 长度最小的子数组](https://leetcode.cn/problems/minimum-size-subarray-sum/) | 中等 | 74 | 2026-07-24 |  |  |  |  |
| 91 | [24. 两两交换链表中的节点](https://leetcode.cn/problems/swap-nodes-in-pairs/) | 中等 | 73 | 2026-06-10 |  |  |  |  |
| 92 | [112. 路径总和](https://leetcode.cn/problems/path-sum/) | 容易 | 72 | 2026-04-14 |  |  |  |  |
| 93 | [139. 单词拆分](https://leetcode.cn/problems/word-break/) | 中等 | 70 | 2026-08-27 |  |  |  |  |
| 94 | [83. 删除排序链表中的重复元素](https://leetcode.cn/problems/remove-duplicates-from-sorted-list/) | 容易 | 69 | 2026-04-23 | ✅ | ★★☆ | [笔记](notes/0083-%E5%88%A0%E9%99%A4%E6%8E%92%E5%BA%8F%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E9%87%8D%E5%A4%8D%E5%85%83%E7%B4%A0/README.md) | [Python](notes/0083-%E5%88%A0%E9%99%A4%E6%8E%92%E5%BA%8F%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E9%87%8D%E5%A4%8D%E5%85%83%E7%B4%A0/solution.py) |
| 95 | [227. 基本计算器 II](https://leetcode.cn/problems/basic-calculator-ii/) | 中等 | 69 | 2026-03-30 |  |  |  |  |
| 96 | [718. 最长重复子数组](https://leetcode.cn/problems/maximum-length-of-repeated-subarray/) | 中等 | 68 | 2026-05-26 |  |  |  |  |
| 97 | [226. 翻转二叉树](https://leetcode.cn/problems/invert-binary-tree/) | 容易 | 68 | 2026-03-29 |  |  |  |  |
| 98 | [169. 多数元素](https://leetcode.cn/problems/majority-element/) | 容易 | 68 | 2026-03-18 |  |  |  |  |
| 99 | [207. 课程表](https://leetcode.cn/problems/course-schedule/) | 中等 | 67 | 2026-07-08 |  |  |  |  |
| 100 | [283. 移动零](https://leetcode.cn/problems/move-zeroes/) | 容易 | 67 | 2026-03-23 | ✅ | ★☆☆ | [笔记](notes/0283-%E7%A7%BB%E5%8A%A8%E9%9B%B6/README.md) | [Python](notes/0283-%E7%A7%BB%E5%8A%A8%E9%9B%B6/solution.py) |
