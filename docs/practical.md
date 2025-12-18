# 快速指南

本页提供京都大学留学生常用的实用信息和资源链接。

## 紧急联系

| 服务 | 电话 | 说明 |
|------|------|------|
| 火警 / 急救 | 119 | 消防与救护车 |
| 警察 | 110 | 紧急报警 |
| 京大保健中心 | 075-753-2411 | 校内医疗咨询 |
| 京大留学生课 | 075-753-2563 | 留学生事务 |

## 实用链接

### 学校资源

- [京都大学官网](https://www.kyoto-u.ac.jp/)
- [国际交流课](https://www.kyoto-u.ac.jp/ja/about/international)
- [学生支援](https://www.kyoto-u.ac.jp/ja/education-campus/student-life)
- [图书馆](https://www.kulib.kyoto-u.ac.jp/)

### 行政手续

- [出入国在留管理庁](https://www.moj.go.jp/isa/index.html) - 签证与在留资格
- [京都市役所](https://www.city.kyoto.lg.jp/) - 住民登记、国保
- [日本年金机构](https://www.nenkin.go.jp/) - 年金减免

### 生活服务

- [京都市垃圾分类](https://www.city.kyoto.lg.jp/kankyo/page/0000000186.html)
- [京都市公交](https://www.city.kyoto.lg.jp/kotsu/)
- [JR 西日本](https://www.westjr.co.jp/)

---

## 本地开发

如果你想参与本 Wiki 的编辑，以下是本地开发环境的配置方法。

### 安装依赖

```shell
# 推荐使用虚拟环境
python3 -m venv .venv
source .venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 本地预览

```shell
mkdocs serve
# 访问 http://127.0.0.1:8000
```

### 构建站点

```shell
mkdocs build
```

### 使用 Docker

```shell
docker compose up
# 访问 http://localhost:8000
```

## 常见问题

??? question "MkDocs 主题未找到"
    ```
    ERROR - Config value 'theme': Unrecognised theme name: 'material'
    ```

    **解决方法**: 确保在正确的 Python 环境中安装依赖:
    ```shell
    pip install -r requirements.txt
    ```

??? question "如何添加新页面"
    1. 在 `docs/` 目录下创建 `.md` 文件
    2. 在 `mkdocs.yml` 的 `nav` 部分添加导航
    3. 运行 `mkdocs serve` 预览

## 编辑约定

- 在 `main` 分支编辑
- 文档源文件在 `docs/`
- 图片放在对应目录的 `assets/images/` 下
- 导航配置在 `mkdocs.yml`

详细贡献指南请参阅 [CONTRIBUTING.md](https://github.com/minamotooRin/KU-WIKI/blob/main/CONTRIBUTING.md)。
