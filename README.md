# KU-WIKI

本WIKI基于[mkdocs.org](https://www.mkdocs.org).
本WIKI基于[mkdocs.org](https://www.mkdocs.org).

欢迎大家一起来施工喵。

NOTE：这是README，主页显示的是`docs/index.html`

## 如何编辑

请在`main`分支下进行编辑。

总之先在`docs`里写文档，`mkdocs.yml`里写目录吧。
图片请在各自的目录下创建`assets/images`。

安装 `mkdocs` 以进行测试：

```shell
pip install mkdocs
```

使用如下指令在本地搭建服务器以测试：

```shell
python -m mkdocs serve
```

使用如下指令编译（？）项目：

```shell
python -m mkdocs build
```

使用如下指令推送项目到`gh-pages`分支（部署用分支）：
```
python -m mkdocs build
```
别忘了再推送到此`main`分支（开发分支）。

使用如下指令打印帮助：

```shell
mkdocs -h
```

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

## 使用Docker构建本地环境

进入到工程目录下，运行下面的命令构建容器

```shell
docker compose up
```

进入到容器内Terminal

```shell
docker compose exec mkdocs bash
```

执行构建命令

```shell
python -m mkdocs build

python -m mkdocs serve -a 0.0.0.0:8000/
```
