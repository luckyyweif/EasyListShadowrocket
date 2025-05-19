#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re
import os

# 规则源 URL 列表
SOURCES = [
    "https://easylist.to/easylist/easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt"
]

def fetch_rules(url):
    """下载并按行拆分规则"""
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    return r.text.splitlines()

def main():
    shadowrocket_rules = []

    for url in SOURCES:
        lines = fetch_rules(url)
        for rule in lines:
            rule = rule.strip()
            # 跳过注释或空行
            if not rule or rule.startswith("!"):
                continue
            # 匹配以 || 开头的规则
            if rule.startswith("||"):
                # 去掉开头 "||"，去掉尾部 "^"
                domain = re.sub(r"\^$", "", rule[2:])
                shadowrocket_rules.append(f"DOMAIN-SUFFIX,{domain},REJECT")

    # 去重并排序
    shadowrocket_rules = sorted(set(shadowrocket_rules))

    # 准备输出目录
    os.makedirs("docs", exist_ok=True)
    out_path = os.path.join("docs", "rules.txt")

    # 写入 [Rule] 表头及所有规则
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("[Rule]\n")
        f.write("\n".join(shadowrocket_rules))

    print(f"Generated {out_path}: {len(shadowrocket_rules)} rules (with [Rule] header)")

if __name__ == "__main__":
    main()
