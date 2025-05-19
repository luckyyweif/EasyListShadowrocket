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

# 输出文件路径
OUTPUT_DIR = "docs"
OUTPUT_FILE = "rules.txt"
SITE_URL = "https://luckyyweif.github.io/EasyListShadowrocket/rules.txt"

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

    # 确保输出目录存在
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)

    # 写入文件：先写头部，再写规则
    with open(out_path, "w", encoding="utf-8") as f:
        # 顶部添加标识行
        f.write(f"#RULE-SET, {SITE_URL}\n")
        # 写入所有规则
        f.write("\n".join(shadowrocket_rules))

    print(f"Generated {out_path}: {len(shadowrocket_rules)} rules")

if __name__ == "__main__":
    main()
