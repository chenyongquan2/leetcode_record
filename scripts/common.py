# -*- coding: utf-8 -*-
"""脚本共享工具：加载题目数据、笔记目录命名、frontmatter 解析。"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "codetop.json")
NOTES_DIR = os.path.join(ROOT, "notes")

LEVEL_NAME = {1: "容易", 2: "中等", 3: "困难"}


def load_questions():
    with open(DATA, encoding="utf-8") as f:
        return json.load(f)["questions"]


def note_dirname(q) -> str:
    """题目 -> 笔记文件夹名，如 0003-无重复字符的最长子串、剑指Offer22-链表中倒数第k个节点。"""
    fid = q["fid"]
    if re.fullmatch(r"\d+", fid):
        prefix = fid.zfill(4)
    else:
        prefix = re.sub(r"[\s\.]+", "", fid)
    name = f"{prefix}-{q['title']}"
    # 去掉 Windows 文件名里的非法字符
    return re.sub(r'[\\/:*?"<>|]+', "", name).strip()


def normalize_fid(s: str) -> str:
    """题号归一化，便于 '剑指 Offer 22' / '剑指Offer22' 都能匹配。"""
    return re.sub(r"[\s\.\-]+", "", s).lower()


def find_question(questions, fid: str):
    key = normalize_fid(fid)
    for q in questions:
        if normalize_fid(q["fid"]) == key:
            return q
    return None


def parse_frontmatter(path: str) -> dict:
    """读取笔记 README.md 开头 --- 包围的 key: value 块。"""
    meta = {}
    try:
        with open(path, encoding="utf-8") as f:
            first = f.readline().strip()
            if first != "---":
                return meta
            for line in f:
                line = line.strip()
                if line == "---":
                    break
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip().strip('"')
    except OSError:
        pass
    return meta


def scan_notes() -> dict:
    """扫描 notes/ 下所有笔记，返回 {归一化题号: 笔记信息}。"""
    result = {}
    if not os.path.isdir(NOTES_DIR):
        return result
    for d in sorted(os.listdir(NOTES_DIR)):
        note_dir = os.path.join(NOTES_DIR, d)
        readme = os.path.join(note_dir, "README.md")
        if not os.path.isfile(readme):
            continue
        meta = parse_frontmatter(readme)
        fid = meta.get("fid")
        if not fid:
            continue
        result[normalize_fid(fid)] = {
            "dir": d,
            "done": meta.get("done", "").lower() in ("true", "yes", "1"),
            "mastery": int(meta.get("mastery") or 0),
            "has_py": os.path.isfile(os.path.join(note_dir, "solution.py")),
            "has_cpp": os.path.isfile(os.path.join(note_dir, "solution.cpp")),
        }
    return result
