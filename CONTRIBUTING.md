# 贡献指南

感谢你对 KU-WIKI 的关注！以下是贡献方式，按难度排序。

---

## 方式一：提交 Issue（最简单）

不需要懂 Git，填写表单即可：

- [新增内容](https://github.com/minamotooRin/KU-WIKI/issues/new?template=new-content.yml) - 提交新文档
- [修改建议](https://github.com/minamotooRin/KU-WIKI/issues/new?template=edit-suggestion.yml) - 建议修改现有内容

---

## 方式二：GitHub 网页编辑

1. 打开 [docs 目录](https://github.com/minamotooRin/KU-WIKI/tree/main/docs)
2. 找到要编辑的文件，点击进入
3. 点击右上角 ✏️ 铅笔图标
4. 编辑后点击 "Propose changes"

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
```

---

## 有问题？

- 提交 [Issue](https://github.com/minamotooRin/KU-WIKI/issues)
- 查看 [FAQ](https://minamotoorin.github.io/KU-WIKI/misc/FAQ/)
