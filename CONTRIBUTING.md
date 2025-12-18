# 贡献指南

感谢你对 KU-WIKI 的关注！本指南帮助你了解如何参与贡献。

## 快速开始

### 1. Fork 仓库

点击 GitHub 页面右上角的 "Fork" 按钮。

### 2. 克隆到本地

```shell
git clone https://github.com/你的用户名/KU-WIKI.git
cd KU-WIKI
```

### 3. 创建分支

```shell
git checkout -b feature/你的功能名
```

### 4. 本地预览

```shell
pip install -r requirements.txt
mkdocs serve
```

访问 http://127.0.0.1:8000 预览更改。

### 5. 提交更改

```shell
git add .
git commit -m "描述你的更改"
git push origin feature/你的功能名
```

### 6. 创建 Pull Request

在 GitHub 上创建 PR，描述你的更改内容。

---

## 文档规范

### 文件结构

```
docs/
├── index.md              # 首页
├── practical.md          # 快速指南
├── visa.md               # 签证
├── housing.md            # 住宿
├── medical.md            # 医疗
├── links.md              # 友情链接
├── about.md              # 关于
├── academic/             # 科研相关
│   ├── index.md
│   └── [专攻名]/
│       ├── index.md
│       └── [研究室].md
├── finance/              # 金融
├── misc/                 # 杂项
│   ├── FAQ.md
│   ├── timeline.md
│   └── ...
└── data/                 # 数据文件
```

### 命名规范

- 文件名使用小写英文或拼音，用 `-` 分隔单词
- 日文名称保持原样（如 `言語メディア処理.md`）
- 图片放在对应目录的 `assets/images/` 下

### 写作风格

- **语言**：中文为主，专有名词保留日文/英文
- **语气**：友好、实用、简洁
- **格式**：使用 Markdown，善用表格、列表、提示框

### Markdown 扩展

本项目使用 Material for MkDocs，支持以下扩展：

```markdown
# 提示框
!!! tip "标题"
    内容

# 可折叠
??? question "问题"
    答案

# 代码高亮
```python
print("Hello")
```

# 表格
| 列1 | 列2 |
|-----|-----|
| A   | B   |
```

---

## 贡献类型

### 内容贡献

- 新增/完善文档页面
- 更新过时信息
- 修正错误
- 添加实用链接

### 技术贡献

- 修复 bug
- 改进 CI/CD
- 优化性能
- 改进样式

### 反馈建议

- 提交 Issue 报告问题
- 建议新功能或新页面
- 参与讨论

---

## 提交规范

### Commit 消息格式

```
类型: 简短描述

详细说明（可选）
```

类型包括：
- `feat`: 新功能
- `fix`: 修复
- `docs`: 文档更新
- `style`: 格式调整
- `refactor`: 重构
- `chore`: 杂项

### 示例

```
docs: 更新签证页面的续签流程

- 添加在线申请链接
- 更新材料清单
```

---

## 行为准则

- 尊重他人
- 保持友善
- 提供建设性反馈
- 遵守 GitHub 社区准则

---

## 需要帮助？

- 查看 [FAQ](docs/misc/FAQ.md)
- 提交 [Issue](https://github.com/minamotooRin/KU-WIKI/issues)
- 联系维护者

感谢你的贡献！
