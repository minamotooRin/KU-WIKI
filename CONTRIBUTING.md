# 贡献指南

感谢你对 KU-WIKI 的关注！无论技术水平如何，你都可以参与贡献。

---

## 方式一：直接在网页编辑（最简单）

**不需要安装任何东西，只需要 GitHub 账号。**

1. 打开 [docs 目录](https://github.com/minamotooRin/KU-WIKI/tree/main/docs)
2. 找到要编辑的 `.md` 文件，点击进入
3. 点击右上角的 ✏️ 铅笔图标
4. 编辑内容（使用 Markdown 格式）
5. 滚动到底部，填写修改说明
6. 点击 "Propose changes"
7. 点击 "Create pull request"

**完成！** 维护者会审核你的修改。

---

## 方式二：本地编辑（推荐频繁贡献者）

```shell
# 1. Fork 并克隆
git clone https://github.com/你的用户名/KU-WIKI.git
cd KU-WIKI

# 2. 安装依赖
pip install -r requirements.txt

# 3. 本地预览
mkdocs serve
# 访问 http://127.0.0.1:8000

# 4. 编辑 docs/ 下的文件

# 5. 提交并推送
git add .
git commit -m "你的修改说明"
git push

# 6. 在 GitHub 上创建 Pull Request
```

---

## 文件放哪里？

| 内容类型 | 位置 |
|---------|------|
| 一般文档 | `docs/` |
| 科研/研究室 | `docs/academic/` |
| 金融相关 | `docs/finance/` |
| 杂项/FAQ | `docs/misc/` |
| 图片 | 对应目录的 `assets/images/` |

**添加新页面？** 编辑 `mkdocs.yml` 的 `nav` 部分添加导航。

---

## 写作建议

- **语言**：中文为主，专有名词保留原文
- **风格**：简洁实用，避免废话
- **格式**：善用表格、列表、提示框

```markdown
<!-- 提示框 -->
!!! tip "提示标题"
    提示内容

<!-- 可折叠 -->
??? question "常见问题"
    答案内容
```

---

## 可以贡献什么？

- ✍️ 完善现有文档
- 📝 新增实用信息
- 🔗 添加有用链接
- 🐛 修正错误
- 💡 提交建议（[Issue](https://github.com/minamotooRin/KU-WIKI/issues)）

---

## 有问题？

- 提交 [Issue](https://github.com/minamotooRin/KU-WIKI/issues)
- 查看 [FAQ](https://minamotoorin.github.io/KU-WIKI/misc/FAQ/)

**感谢你的贡献！**
