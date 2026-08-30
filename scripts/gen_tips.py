# -*- coding: utf-8 -*-
"""汇总 notes/ 各题笔记中的「## 知识点：…」小节，生成 TIPS.md 集中复习页。

用法:
    python scripts/gen_tips.py
（gen_readme.py 会自动调用，通常不需要单独运行。）
"""
import os
import re
import time
from urllib.parse import quote

from common import NOTES_DIR, ROOT, parse_frontmatter

HEADING = re.compile(r"^##\s*知识点[：:]\s*(.+)$")


def extract_tips(readme_path: str):
    """返回 [(标题, 正文)]，正文为该小节到下一个 ## 级标题之前的内容。"""
    with open(readme_path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    tips = []
    title, body = None, []

    def flush():
        if title is not None:
            tips.append((title, "\n".join(body).strip()))

    for line in lines:
        m = HEADING.match(line)
        if m:
            flush()
            title, body = m.group(1).strip(), []
        elif line.startswith("## "):
            flush()
            title, body = None, []
        elif title is not None:
            body.append(line)
    flush()
    return tips


def main() -> None:
    entries = []  # (目录名, fid, 题名, [(标题, 正文), ...])
    if os.path.isdir(NOTES_DIR):
        for d in sorted(os.listdir(NOTES_DIR)):
            readme = os.path.join(NOTES_DIR, d, "README.md")
            if not os.path.isfile(readme):
                continue
            tips = extract_tips(readme)
            if not tips:
                continue
            meta = parse_frontmatter(readme)
            entries.append((d, meta.get("fid", "?"), meta.get("title", d), tips))

    total = sum(len(e[3]) for e in entries)
    today = time.strftime("%Y-%m-%d")
    out = [
        "# 易错知识点汇总",
        "",
        "从各题笔记的「`## 知识点：…`」小节自动汇总，用于集中复习。",
        "内容请在对应题目的笔记里修改，然后运行 `python scripts/gen_readme.py` 重新生成本页。",
        "",
        f"**共 {total} 条，来自 {len(entries)} 道题**　（更新于 {today}）",
        "",
    ]
    for d, fid, title, tips in entries:
        out.append(f"## {fid}. {title}")
        out.append("")
        for tip_title, body in tips:
            out.append(f"### {tip_title}")
            out.append("")
            if body:
                out.append(body)
                out.append("")
        out.append(f"> 出处：[{fid}. {title} 的笔记](notes/{quote(d)}/README.md)")
        out.append("")
    with open(os.path.join(ROOT, "TIPS.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"已生成 TIPS.md（{total} 条知识点，来自 {len(entries)} 道题）")


if __name__ == "__main__":
    main()
