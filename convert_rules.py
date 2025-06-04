#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re
import os

# 规则源 URL 列表
SOURCES = [
    "https://easylist.to/easylist/easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt"
    "https://raw.githubusercontent.com/easylist/easylistchina/refs/heads/master/easylistchina.txt"
]

def fetch_rules(url):
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    return r.text.splitlines()

def main():
    shadowrocket_rules = []

    for url in SOURCES:
        lines = fetch_rules(url)
        for rule in lines:
            rule = rule.strip()
            if not rule or rule.startswith("!"):
                continue
            if rule.startswith("||"):
                # 去掉开头 "||"，去掉尾部 "^"
                domain = re.sub(r"\^$", "", rule[2:])
                shadowrocket_rules.append(f"DOMAIN-SUFFIX,{domain},REJECT")

    # 去重并排序
    shadowrocket_rules = sorted(set(shadowrocket_rules))

    # 输出到 docs/rules.txt
    os.makedirs("docs", exist_ok=True)
    out_path = os.path.join("docs", "rules.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(shadowrocket_rules))

    print(f"Generated {out_path}: {len(shadowrocket_rules)} rules")

if __name__ == "__main__":
    main()
