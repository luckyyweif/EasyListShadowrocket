# EasyListShadowrocket

本仓库每天自动从 EasyList 和 EasyPrivacy 下载广告和跟踪器规则，转换成 Shadowrocket / Clash 等支持的纯文本格式（`DOMAIN-SUFFIX,域名,REJECT`），并通过 GitHub Pages 发布。

- 🔗 **EasyList 源**：https://easylist.to/easylist/easylist.txt  
- 🔗 **EasyPrivacy 源**：https://easylist.to/easylist/easyprivacy.txt  
- 📄 **输出文件**：`rules.txt`（发布于 GitHub Pages）  
- 🚀 **访问链接**：https://luckyyweif.github.io/EasyListShadowrocket/rules.txt  

## 使用方法

1. 直接通过上面的链接获取最新的 `rules.txt`。  
2. 导入到 Shadowrocket、Clash 或其他支持域名后缀规则的工具中。  
3. 如需手动刷新，进入仓库 **Actions** → 找到 “每日更新 EasyList 规则” → 点击 **Run workflow**。

## 项目结构
├── .github/
│ └── workflows/
│ └── update-rules.yml # 自动下载并转换规则的 GitHub Actions 配置
├── docs/
│ ├── rules.txt # 最终发布的纯文本规则集
│ └── .nojekyll # 禁用 Jekyll，直接发布静态文件
├── convert_rules.py # 下载并转换规则的 Python 脚本
└── README.md # 本说明文档

## 贡献 & 协议

- 欢迎提交 Issue、Pull Request；也可以在 Discussions 中讨论。  
- 本项目使用 [MIT License](LICENSE)（如需请自行添加 LICENSE 文件）。

---

> 本项目由 GitHub Actions 自动维护，保证每天更新，0 依赖、0 运维。  
