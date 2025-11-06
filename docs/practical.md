# 快速指南与实用信息（Quick Start & Practical Info）

## 快速开始（推荐：使用虚拟环境）

1. 在项目根目录创建并激活虚拟环境（可选，但推荐）：

```shell
python3 -m venv .venv
source .venv/bin/activate
```

1. 安装项目依赖（`requirements.txt` 已包含 `mkdocs` 与 `mkdocs-material`）：

```shell
python3 -m pip install -r requirements.txt
```

1. 本地预览（开发服务器，保存后会自动刷新）：

```shell
python3 -m mkdocs serve
# 访问 http://127.0.0.1:8000
```

1. 构建静态站点输出到 `site/`：

```shell
python3 -m mkdocs build
```

如果你不想单独安装依赖，也可以直接使用 Docker（见下文）。

## 实用链接（起点）

- 京都大学国际交流中心（International Student Office） — 学校官方支持与咨询
- 京都大学研究生院/各学院官网 — 学术事务与学位指南
- 入国管理局（出入国在留管理庁） — 在留资格与签证信息
- 京都市役所 — 居住登记、国民健康保险
- 日本全国健康保险/医疗信息站点

（我可以把上面的外部链接具体化并列出官方 URL，或把这些主题拆分为各自页面并在 `mkdocs.yml` 中建立导航）


## 紧急联系与常用电话（建议本地保留）

- 火警 / 救急（消防）: 119
- 警察（紧急）: 110
- 最近大学医院/急诊电话：请在各学院页面或本地信息页注明（我可以帮你补全具体院校医院电话）
- 京都大学国际交流处（学校内部紧急联系）: （这里填写学校内线和邮箱的建议位置）

## 常见问题（FAQ）示例

- Q: 刚到日本，医疗如何就诊？ — A: 首先完成居民登记并加入国民健康保険（国保），带上在留卡与健康保险证前往医院或诊所就诊；若为紧急情况，直接拨打119。
- Q: 可以在读期间打工吗？如何申请？ — A: 留学生可在部分条件下打工，须获取“資格外活動許可”（或确认在留资格允许工作），并遵守每周工作时间限制。校内兼职通常通过实验室或学院公告。税务与报酬请留意发票与报税义务。

## 如何贡献

1. 提交 Issue：如果你发现信息过时或希望增加某个话题，请在仓库中开 Issue。
2. 提交 PR：编辑 `docs/` 下的相应页面并提交 Pull Request；建议在 `main` 分支以外新建分支进行修改。
3. 想让我们帮你搭建专题页？告诉我你需要的主题，我可以帮你创建基本子页（例如 `docs/visa.md`、`docs/housing.md`）并更新 `mkdocs.yml`。

---

如果你愿意，我现在可以：

- A) 把本页变得更精简/更正式的版本（例如加入更多官方链接与联系方式）;
- B) 为优先主题（例如“签证”、“住宿”、“紧急联系人”）创建独立子页面并把它们加入导航;
- C) 帮你把所有外部官方 URL 补全并加入“实用链接”列表。

## 常见问题（Troubleshooting）

- 错误：

    ```text
    ERROR - Config value 'theme': Unrecognised theme name: 'material'. The available installed themes are: mkdocs, readthedocs
    ```

    解决方法：确保你在运行 `mkdocs` 的同一 Python 解释器里安装了 `mkdocs-material`：

    ```shell
    python3 -m pip install mkdocs-material
    # 或者安装全部依赖
    python3 -m pip install -r requirements.txt
    ```

    注意：如果使用系统 `mkdocs`（例如通过 Homebrew 安装）可能会调用不同的 Python。建议使用 `python3 -m mkdocs` 与 `python3 -m pip` 保证一致性，或在虚拟环境中操作。

## 如何编辑与约定

- 请在 `main` 分支下编辑文档，完成后推送并发起 PR（如果有必要）。
- 文档源文件放在 `docs/` 下；站点输出在 `site/`。
- 页面目录由 `mkdocs.yml` 管理。请在 `mkdocs.yml` 的 `nav` 中添加新页面。
- 图片请放在对应目录的 `assets/images/`（例如 `docs/academic/社会情报学/assets/images/`）。

---

感谢参与！有问题可以在仓库里开 issue 或直接发 PR。
