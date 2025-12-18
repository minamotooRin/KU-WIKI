# KU-WIKI

京都大学中文学生指南 - 基于 [MkDocs](https://www.mkdocs.org) 和 [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) 构建。

欢迎大家一起来施工喵。

> **注意**: 这是 README，网站主页内容在 `docs/index.md`

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

1. 在 `main` 分支下进行编辑
2. 文档放在 `docs/` 目录
3. 图片放在对应文档目录的 `assets/images/` 下
4. 导航配置在 `mkdocs.yml` 的 `nav` 部分

详细贡献指南请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。

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

## 许可

本项目内容仅供参考，不代表官方立场。
