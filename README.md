# KU-WIKI

京都大学中文学生指南 - 欢迎大家一起来施工喵。

## 什么是 MkDocs？

本项目使用 [MkDocs](https://www.mkdocs.org) 构建，这是一个将 Markdown 文件转换成网站的工具。

**你只需要知道：**
- 所有文档都是 `.md` 文件（Markdown 格式，类似纯文本）
- 编辑 `docs/` 文件夹里的 `.md` 文件 → 网站内容就会更新
- 不需要懂 HTML/CSS/JavaScript

## 快速开始

### 安装依赖

```shell
pip install -r requirements.txt
```

### 本地预览

```shell
mkdocs serve
```

访问 http://127.0.0.1:8000 预览网站。

### 构建静态文件

```shell
mkdocs build
```

## 如何贡献

### 🌟 最简单：直接在 GitHub 上编辑（推荐新手）

1. 在 [docs 目录](https://github.com/minamotooRin/KU-WIKI/tree/main/docs) 找到要编辑的文件
2. 点击文件，然后点击右上角的 ✏️ 编辑按钮
3. 修改内容，填写说明，点击 "Propose changes"
4. 完成！维护者会审核你的修改

### 🔧 进阶：Fork 后提交 PR

1. Fork 本仓库到你的账号
2. 在你的仓库中编辑 `docs/` 下的文件
3. 提交 Pull Request

### 📝 编辑须知

- **文档位置**：`docs/` 目录
- **图片位置**：对应目录的 `assets/images/` 下
- **添加新页面**：需要在 `mkdocs.yml` 的 `nav` 部分添加导航

## 项目结构

```
mkdocs.yml          # MkDocs 配置文件
docs/
  index.md          # 网站首页
  academic/         # 科研相关
  finance/          # 金融服务
  misc/             # 杂项
  ...
scripts/            # 自动化脚本
```

## 使用 Docker

```shell
# 启动容器
docker compose up

# 进入容器
docker compose exec mkdocs bash

# 在容器内启动服务
mkdocs serve --dev-addr 0.0.0.0:8000
```

## 部署

推送到 `main` 分支后，GitHub Actions 会自动构建并部署到 GitHub Pages。

### 手动部署

```shell
mkdocs build
mkdocs gh-deploy
```

## 许可

本项目内容仅供参考，不代表官方立场。
