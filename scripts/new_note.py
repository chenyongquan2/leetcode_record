# -*- coding: utf-8 -*-
"""为一道题创建笔记脚手架：notes/题号-题名/{README.md, solution.py, solution.cpp}，
然后自动重新生成 README.md / PROBLEMS.md 表格。

用法:
    python scripts/new_note.py 3
    python scripts/new_note.py 剑指Offer22
    python scripts/new_note.py 补充题4
"""
import os
import sys

import gen_readme
from common import LEVEL_NAME, NOTES_DIR, ROOT, find_question, load_questions, note_dirname

NOTE_TEMPLATE = """---
fid: "{fid}"
title: {title}
done: true
mastery: 1
---

# {fid}. {title}

- 难度：{level}　|　CodeTop 频率：{frequency}
- 链接：{link}

## 思路

（写下核心思路、关键观察）

## 复杂度

- 时间：O()
- 空间：O()

## 易错点 / 回顾记录

- {today}：首次完成。
"""

PY_TEMPLATE = '''# {fid}. {title}
# {link}


class Solution:
    pass
'''

CPP_TEMPLATE = """// {fid}. {title}
// {link}

class Solution {{
public:
}};
"""


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    fid = " ".join(sys.argv[1:])
    q = find_question(load_questions(), fid)
    if not q:
        print(f"在 data/codetop.json 中没找到题号「{fid}」")
        sys.exit(1)

    note_dir = os.path.join(NOTES_DIR, note_dirname(q))
    link = f"https://leetcode.cn/problems/{q['slug']}/" if q["slug"] else "（无 LeetCode 链接）"
    ctx = {
        "fid": q["fid"],
        "title": q["title"],
        "level": LEVEL_NAME.get(q["level"], "?"),
        "frequency": q["frequency"],
        "link": link,
        "today": __import__("time").strftime("%Y-%m-%d"),
    }

    os.makedirs(note_dir, exist_ok=True)
    created = []
    for fname, template in (
        ("README.md", NOTE_TEMPLATE),
        ("solution.py", PY_TEMPLATE),
        ("solution.cpp", CPP_TEMPLATE),
    ):
        path = os.path.join(note_dir, fname)
        if os.path.exists(path):
            continue
        with open(path, "w", encoding="utf-8") as f:
            f.write(template.format(**ctx))
        created.append(fname)

    rel = os.path.relpath(note_dir, ROOT)
    if created:
        print(f"已创建 {rel}\\{{{', '.join(created)}}}")
    else:
        print(f"{rel} 已存在，未覆盖任何文件")
    gen_readme.main()


if __name__ == "__main__":
    main()
