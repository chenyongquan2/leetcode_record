# -*- coding: utf-8 -*-
"""从 codetop.cc 抓取题目列表（频率、难度、最近考察时间），保存到 data/codetop.json。

用法:
    python scripts/fetch_codetop.py

如果想同时带上你在 codetop 上的个人数据（是否完成 status / 掌握程度 rate），
登录 codetop.cc 后从浏览器开发者工具里复制请求头，设置环境变量后再运行:
    $env:CODETOP_COOKIE = "<Cookie 请求头的完整值>"
    $env:CODETOP_AUTH   = "<Authorization 请求头的值，如果有>"
"""
import json
import os
import sys
import time
import urllib.request

API = "https://codetop.cc/api/questions/?page={page}&page_size=20&search=&ordering=-frequency"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "application/json",
}

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "codetop.json")


def fetch_page(page: int) -> dict:
    req = urllib.request.Request(API.format(page=page), headers=HEADERS)
    cookie = os.environ.get("CODETOP_COOKIE")
    auth = os.environ.get("CODETOP_AUTH")
    if cookie:
        req.add_header("Cookie", cookie)
    if auth:
        req.add_header("Authorization", auth)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main() -> None:
    first = fetch_page(1)
    total = first["count"]
    pages = (total + 19) // 20
    print(f"共 {total} 题，{pages} 页")

    questions = []
    seen = set()
    page = 1
    data = first
    while True:
        for item in data["list"]:
            lc = item["leetcode"]
            qid = lc["frontend_question_id"]
            if qid in seen:
                continue
            seen.add(qid)
            questions.append(
                {
                    "fid": qid,                          # 题号（LeetCode 前端编号）
                    "title": lc["title"],                # 标题
                    "slug": lc.get("slug_title") or "",  # LeetCode 链接 slug
                    "level": lc["level"],                # 1 容易 / 2 中等 / 3 困难
                    "frequency": item["value"],          # 出现频率
                    "last_asked": (item.get("time") or "")[:10],  # 最近考察日期
                    "codetop_status": bool(item.get("status")),   # codetop 上的完成状态(需登录)
                    "codetop_rate": item.get("rate") or 0,        # codetop 上的掌握程度(需登录)
                }
            )
        sys.stdout.write(f"\r已抓取第 {page}/{pages} 页，共 {len(questions)} 题")
        sys.stdout.flush()
        if page >= pages:
            break
        page += 1
        time.sleep(0.4)
        data = fetch_page(page)
    print()

    questions.sort(key=lambda q: -q["frequency"])
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(
            {"fetched_at": time.strftime("%Y-%m-%d"), "count": len(questions), "questions": questions},
            f,
            ensure_ascii=False,
            indent=1,
        )
    print(f"已保存到 {os.path.relpath(OUT, ROOT)}")


if __name__ == "__main__":
    main()
