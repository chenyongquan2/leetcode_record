# -*- coding: utf-8 -*-
"""根据 data/codetop.json + notes/ 下的笔记，生成 README.md（Top 100）和 PROBLEMS.md（全部题目）。

用法:
    python scripts/gen_readme.py
"""
import os
import time
from urllib.parse import quote

import gen_tips
from common import LEVEL_NAME, ROOT, load_questions, normalize_fid, scan_notes

TOP_N = 100


def leetcode_link(q) -> str:
    if q["slug"]:
        return f"[{q['fid']}. {q['title']}](https://leetcode.cn/problems/{q['slug']}/)"
    return f"{q['fid']}. {q['title']}"


# codetop 网站的掌握程度是 0-3 制，折算到本仓库的 5 分制
CODETOP_RATE_TO_5 = {0: 0, 1: 1, 2: 3, 3: 5}


def row(rank: int, q, note) -> str:
    done = "✅" if (note and note["done"]) or q.get("codetop_status") else ""
    rate5 = CODETOP_RATE_TO_5.get(q.get("codetop_rate") or 0, 0)
    mastery = min(max(note["mastery"] if note else 0, rate5), 5)
    stars = "★" * mastery + "☆" * (5 - mastery) if (note or mastery) else ""
    if note:
        d = quote(note["dir"])
        note_link = f"[笔记](notes/{d}/README.md)"
        sols = []
        if note["has_py"]:
            sols.append(f"[Python](notes/{d}/solution.py)")
        if note["has_cpp"]:
            sols.append(f"[C++](notes/{d}/solution.cpp)")
        sol_link = " / ".join(sols)
    else:
        note_link = ""
        sol_link = ""
    return (
        f"| {rank} | {leetcode_link(q)} | {LEVEL_NAME.get(q['level'], '?')} "
        f"| {q['frequency']} | {q['last_asked']} | {done} | {stars} | {note_link} | {sol_link} |"
    )


def table(questions, notes) -> str:
    lines = [
        "| # | 题目 | 难度 | 频率 | 最近考察 | 完成 | 掌握 | 笔记 | 题解 |",
        "|---:|---|---|---:|---|:---:|---|---|---|",
    ]
    for i, q in enumerate(questions, 1):
        lines.append(row(i, q, notes.get(normalize_fid(q["fid"]))))
    return "\n".join(lines)


def main() -> None:
    questions = load_questions()
    notes = scan_notes()
    done_count = sum(
        1
        for q in questions
        if q.get("codetop_status")
        or (notes.get(normalize_fid(q["fid"])) or {}).get("done")
    )
    today = time.strftime("%Y-%m-%d")

    readme = f"""# LeetCode 刷题笔记

按 [CodeTop](https://codetop.cc/home) 面试频率排序的刷题记录。每道题一个文件夹（`notes/题号-题名/`），
包含笔记 `README.md` 和 `solution.py` / `solution.cpp` 两种语言的题解。

**进度：{done_count} / {len(questions)}**　（数据更新于 {today}，完整列表见 [PROBLEMS.md](PROBLEMS.md)，易错知识点汇总见 [TIPS.md](TIPS.md)）

## 使用方法

**方式一（推荐）：** 直接把「题号 + 题解代码（Python/C++）+ 思路（可选）」发给 Claude Code，
它会按项目 skill [record-note](.claude/skills/record-note/SKILL.md) 自动录入笔记、刷新表格并提交。

**方式二：手动操作**

```bash
# 刷完一道题后，新建这道题的笔记（按题号，如 3、146、"剑指Offer22"、"补充题4"）
python scripts/new_note.py 3

# 在 notes/0003-无重复字符的最长子串/ 里写笔记和题解，
# 并在其 README.md 顶部 frontmatter 中维护 done（是否完成）和 mastery（掌握程度 0-5）

# 重新生成本页和 PROBLEMS.md 的表格
python scripts/gen_readme.py

# 更新 CodeTop 频率数据（可选：设置 CODETOP_COOKIE 环境变量可同步你在 codetop 上的完成/掌握状态）
python scripts/fetch_codetop.py && python scripts/gen_readme.py
```

## 高频 Top {TOP_N}

{table(questions[:TOP_N], notes)}
"""

    problems = f"""# 全部题目（{len(questions)} 题）

按 CodeTop 面试频率降序排列，数据更新于 {today}。高频 Top {TOP_N} 见 [README.md](README.md)。

{table(questions, notes)}
"""

    with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme)
    with open(os.path.join(ROOT, "PROBLEMS.md"), "w", encoding="utf-8") as f:
        f.write(problems)
    print(f"已生成 README.md（Top {TOP_N}）和 PROBLEMS.md（{len(questions)} 题），进度 {done_count}/{len(questions)}")
    gen_tips.main()


if __name__ == "__main__":
    main()
