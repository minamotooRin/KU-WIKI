# 贡献指南

感谢你对 KU-WIKI 的关注！以下是三种贡献方式，按难度排序。

---

## 方式一：可视化编辑（推荐）

访问 [在线编辑器](https://minamotoorin.github.io/KU-WIKI/admin/) → GitHub 登录 → 选择分类 → 编辑 → 保存

所有修改会自动创建 PR，维护者审核后发布。

---

## 方式二：提交 Issue

不想登录编辑器？直接提交 Issue：

- [新增内容](https://github.com/minamotooRin/KU-WIKI/issues/new?template=new-content.yml)
- [修改建议](https://github.com/minamotooRin/KU-WIKI/issues/new?template=edit-suggestion.yml)

---

## 方式三：Git 流程

1. Fork 本仓库
2. 编辑 `docs/` 下的文件
3. 提交 Pull Request

### 文件位置

| 内容 | 目录 |
|------|------|
| 一般文档 | `docs/` |
| 科研 | `docs/academic/` |
| 金融 | `docs/finance/` |
| 杂项 | `docs/misc/` |

### 本地预览

```shell
pip install -r requirements.txt
mkdocs serve
# 访问 http://127.0.0.1:8000
```

---

## 有问题？

- 提交 [Issue](https://github.com/minamotooRin/KU-WIKI/issues)
- 查看 [FAQ](https://minamotoorin.github.io/KU-WIKI/misc/FAQ/)
