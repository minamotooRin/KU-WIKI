# KU-WIKI
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
```
pip install mkdocs
```

使用如下指令在本地搭建服务器以测试：
```
python -m mkdocs serve
```

使用如下指令编译（？）项目：
```
python -m mkdocs build
```

使用如下指令推送项目到`gh-pages`分支（部署用分支）：
```
python -m mkdocs build
```
别忘了再推送到此`main`分支（开发分支）。

使用如下指令打印帮助：
```
mkdocs -h
```

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
