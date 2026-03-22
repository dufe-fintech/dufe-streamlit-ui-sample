# Sample Streamlit UI App (Powered by uv)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![uv](https://img.shields.io/badge/managed%20with-uv-6e56cf)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)
![Pandas](https://img.shields.io/badge/data-Pandas-150458)

一个**非常适合初学者**的 Streamlit 小项目，用来演示如何用 Python 快速搭建一个简单的交互式 Web 页面。  

这个项目也特别适合课堂教学，因为你可以完整展示下面这条流程：

Fork 项目 -> Clone 到本地 -> 使用 uv 管理依赖 -> 本地运行 -> 在浏览器中查看效果

--------------------------------------------------
Project Overview
--------------------------------------------------
作者：刘老师（fintechlab@dufe.edu.cn）

这是一个简单的 Streamlit Web App，主要用于帮助初学者认识常见的交互式组件（widgets）是如何工作的。

运行后，你可以在页面中完成这些操作：

- 输入你的姓名
- 用滑块选择年龄
- 从下拉框中选择你喜欢的工具
- 上传一个 CSV 文件并预览数据内容

这个项目非常适合：

- Python 初学者
- 第一次接触 Streamlit 的同学
- 想学习 uv 基本用法的同学
- 想练习“如何把 GitHub 项目拉到本地并运行起来”的同学
- 课堂教学演示

--------------------------------------------------
Features
--------------------------------------------------

本项目包含以下功能：

- st.title() + st.write()
  显示页面标题和文本内容

- st.text_input()
  输入姓名

- st.slider()
  选择年龄

- st.selectbox()
  从下拉菜单中选择喜欢的工具

- st.file_uploader()
  上传 CSV 文件

- pandas.read_csv()
  读取并预览上传的数据内容

--------------------------------------------------
What You Will Learn
--------------------------------------------------

通过这个项目，你可以顺便掌握这些基础技能：

- 如何从 GitHub 获取一个 Python 项目
- 如何进入项目目录并查看项目文件
- 如何使用 uv 管理项目依赖
- 如何在本地运行一个 Streamlit 项目
- 如何理解“项目环境”和“依赖安装”的基本思路

--------------------------------------------------
Tech Stack
--------------------------------------------------

本项目使用了以下工具：

- Python
- uv
- Streamlit
- Pandas

--------------------------------------------------
How to Run the App
--------------------------------------------------

下面演示如何使用 uv 在本地运行这个项目。

1）Fork 本项目

如果你想把这个项目放到你自己的 GitHub 仓库下面，建议先进行 Fork。

操作方法：

1. 打开这个项目的 GitHub 页面
2. 点击右上角 Fork
3. 选择你的 GitHub 账号
4. Fork 完成后，你就会在自己的仓库下拥有一个副本

这样做的好处是：

- 你可以自由修改 README
- 你可以把它变成自己的教学示例项目
- 你可以继续提交、维护、扩展这个仓库

2）Clone 你的仓库到本地

把下面命令中的仓库地址替换成你自己的(dufe-fintech->你的github名字)：

```bash
git clone https://github.com/dufe-fintech/dufe-streamlit-ui-sample.git
cd dufe-streamlit-ui-sample
```

如果你不确定仓库地址，可以在 GitHub 仓库首页点击绿色 Code 按钮，然后复制 HTTPS 地址。

3）检查是否已经安装 uv

先检查你的电脑中是否已经安装了 uv：

uv --version

如果终端能够显示版本号，说明已经安装成功。
如果没有安装，请先安装 uv。

macOS / Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows PowerShell
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

安装完成后，建议重新打开终端，再次检查：

```bash
uv --version
```

4）进入项目目录并查看文件

进入项目目录后，你可以先看一下目录中有哪些文件。

macOS / Linux
```bash
ls
```

Windows PowerShell
```bash
dir
```

你通常会看到类似这样的文件：

- Sample.py
- README.md

当你后续使用 uv 初始化并安装依赖后，还会看到：

- pyproject.toml
- uv.lock
- .venv/

5）用 uv 初始化项目

在项目目录中运行：
```bash
uv init
```
这一句可以简单理解为：

告诉 uv：从现在开始，这个目录是一个 Python 项目，请帮我管理它。

运行后，项目中通常会出现 pyproject.toml。
后续当你执行项目相关命令时，uv 还会自动创建 .venv 和 uv.lock。

6）安装项目依赖

本项目需要的核心依赖是：

- streamlit
- pandas

安装命令如下：
```bash
uv add streamlit pandas
```
这一句和传统的 pip install ... 有一点区别：

- pip install 主要是把包装到当前环境里
- uv add 不仅会安装包，还会把依赖记录到项目配置中

这样以后别人拿到这个项目时，更容易复现你的环境。

7）运行项目

执行下面命令启动应用：
```bash
uv run streamlit run Sample.py
```

运行成功后，终端通常会显示类似下面的本地地址：
```bash
http://localhost:8501
```

然后你可以在浏览器中打开这个地址，就能看到页面效果。

8）快速运行版

如果你的电脑已经安装好了 uv，那么从 clone 到运行，可以直接依次执行下面命令：
```bash
git clone https://github.com/dufe-fintech/dufe-streamlit-ui-sample.git
cd dufe-streamlit-ui-sample
uv init
uv add streamlit pandas
uv run streamlit run Sample.py
```

--------------------------------------------------
Project Structure
--------------------------------------------------

一个典型的项目目录大致如下：

dufe-streamlit-ui-sample/
├── Sample.py
├── README.md
├── pyproject.toml
├── uv.lock
└── .venv/

说明：

- Sample.py：项目主程序
- README.md：项目说明文档
- pyproject.toml：项目配置文件，记录项目信息和依赖
- uv.lock：依赖锁定文件，帮助复现一致环境
- .venv/：项目虚拟环境目录

如果你是第一次接触这些文件，可以先这样理解：

- pyproject.toml：项目需要哪些依赖
- .venv/：项目自己的独立 Python 环境
- uv.lock：记录当前依赖版本，方便以后复现

--------------------------------------------------
What Each Command Does
--------------------------------------------------

这里对核心命令做一个非常初学者友好的解释。
```bash
git clone
```

把 GitHub 上的项目下载到本地电脑。

```bash
cd dufe-streamlit-ui-sample
```

进入项目文件夹。

```bash
uv init
```

把当前目录初始化为一个由 uv 管理的 Python 项目。

```bash
uv add streamlit pandas
```

安装依赖，并把依赖记录到项目配置中。

```bash
uv run streamlit run Sample.py
```

在项目环境中运行 Streamlit 程序。

--------------------------------------------------
What You Should See
--------------------------------------------------

项目启动后，你会在浏览器中看到一个简单的交互式页面，通常包含：

- 页面标题
- 姓名输入框
- 年龄滑块
- 工具选择下拉框
- CSV 上传区域
- 上传后显示的数据预览

这也是本项目非常适合教学的原因：

它不复杂，但结果非常直观。

学生很容易理解：

原来 Python 不只是写命令行程序，也可以很方便地做一个简单的网页界面。

--------------------------------------------------
Why Use uv?
--------------------------------------------------

对于初学者来说，uv 有几个比较直观的优点：

- 命令简洁
- 依赖管理更统一
- 项目环境更清晰
- 更适合“一个项目一个环境”的习惯
- 很适合课堂上演示标准项目流程

你可以先把它简单理解成：

uv 是一个更现代、更整洁的 Python 项目与依赖管理工具。

--------------------------------------------------
Common Issues
--------------------------------------------------

1. 终端提示找不到 uv

可能原因：

- 还没有安装 uv
- 安装后没有重新打开终端
- uv 没有加入系统 PATH

可以先检查：
```bash
uv --version
```

如果还不行，请重新安装一次，并重新打开终端。

2. 浏览器没有自动打开

没关系，手动在浏览器输入下面地址即可：

http://localhost:8501

3. Sample.py 找不到怎么办？

请先确认项目目录中是否真的存在这个文件。

macOS / Linux
```bash
ls
```

Windows PowerShell
```bash
dir
```

如果文件名不是 Sample.py，请按实际文件名修改运行命令，例如：
```bash
uv run streamlit run your_file_name.py
```

4. CSV 文件上传后没有显示内容

请检查：

- 上传的是否是 .csv 文件
- CSV 文件是否为空
- 文件编码是否正常
- 代码中是否正确使用了 pandas.read_csv()

5. 端口被占用了怎么办？

如果 8501 端口已经被其他程序占用，可以换一个端口运行：

uv run streamlit run Sample.py --server.port 8502

然后在浏览器中访问：

http://localhost:8502

--------------------------------------------------
Classroom Demo Suggestion
--------------------------------------------------

如果你是老师，或者想在课堂上做展示，可以按下面顺序来讲：

1. 这是一个什么项目
2. 先 Fork 到自己的仓库
3. 再 Clone 到本地
4. 用 uv init 把它变成 uv 管理的项目
5. 用 uv add 安装依赖
6. 用 uv run 本地启动
7. 在浏览器中查看效果
8. 让学生自己修改一个小地方并重新运行

例如，你可以让学生试着修改：

- 页面标题
- 下拉框选项
- 默认文本
- 上传后的提示信息

这样他们会更有参与感。

--------------------------------------------------
Practice Ideas
--------------------------------------------------

你可以给学生布置一些很简单的小练习：

练习 1：修改页面标题

把页面标题改成你自己的名字，例如：

- Alice's Streamlit App
- My First Streamlit UI

练习 2：修改下拉框选项

把下拉框中的工具选项改成你熟悉的软件，例如：

- Python
- VS Code
- Jupyter Notebook
- GitHub

练习 3：上传自己的 CSV 文件

自己创建一个 CSV 文件并上传，观察页面如何显示数据。

--------------------------------------------------
Future Scope
--------------------------------------------------

这个项目后续可以继续扩展成更完整的练习项目，例如：

- 增加数据可视化
- 支持 Excel 文件上传
- 加入图片上传
- 使用 st.sidebar() 增加侧边栏
- 使用 pages/ 做多页面应用
- 做一个简单的数据分析展示板

--------------------------------------------------
Demo Screenshot
--------------------------------------------------

你可以把运行截图放在这里，例如：

![Demo Screenshot](./assets/demo.png)

--------------------------------------------------
Suggested Git Commits
--------------------------------------------------

如果你在教学中一步一步演示，也可以顺手做几次提交，例如：
```bash
git add .
git commit -m "init project with uv"
git commit -m "add streamlit and pandas with uv"
git commit -m "update README for uv workflow"
```

这样就能够顺便看到 Git 的基本使用流程。

--------------------------------------------------
License
--------------------------------------------------

This project is for learning, teaching, and demonstration purposes.

You may choose an open-source license if needed, such as:

- MIT License
- Apache License 2.0

--------------------------------------------------
A Note for Beginners
--------------------------------------------------

如果你是第一次看到这个项目，请记住：

你现在不需要一次性搞懂所有内容。
你只需要先把这几件事做成功：

- 把项目下载下来
- 安装依赖
- 成功运行
- 在浏览器中看到页面

只要做到这一步，你就已经完成了一次非常重要的实践。

学习编程最好的方式之一就是：

先跑起来，再慢慢看懂。

**祝你学习顺利、玩得开心！**

*有问题请联系：*
**刘老师（fintechlab@dufe.edu.cn）**


