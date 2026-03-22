# Sample Streamlit UI App (Powered by uv)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![uv](https://img.shields.io/badge/managed%20with-uv-6e56cf)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)
![Pandas](https://img.shields.io/badge/data-Pandas-150458)

一个**非常适合初学者**的 Streamlit 小项目，用来演示如何用 Python 快速搭建一个简单的交互式 Web 页面。  

这个项目也特别适合课堂教学，因为你可以完整展示下面这条开发流程：

> 从 GitHub 获取项目 → 进入项目目录 → 使用 `uv` 管理依赖 → 本地运行项目 → 在浏览器中查看效果

---

## 作者：

刘老师

---

## 项目简介

这是一个简单的 Streamlit Web App，主要用于帮助初学者认识常见的交互式组件（widgets）是如何工作的。

运行后，你可以在页面中完成这些操作：

- 输入你的姓名
- 用滑块选择年龄
- 从下拉框中选择你喜欢的工具
- 上传一个 CSV 文件并预览数据内容

这个项目非常适合：

- Python 初学者
- 第一次接触 Streamlit 的同学
- 想学习 `uv` 基本用法的同学
- 课堂演示“如何把 GitHub 项目拉到本地并运行起来”的老师和学生

---

## 你将学到什么

通过这个项目，你可以顺便掌握这些基础技能：

- 如何从 GitHub 获取一个 Python 项目
- 如何进入项目目录并查看项目文件
- 如何使用 `uv` 管理项目依赖
- 如何在本地运行一个 Streamlit 项目
- 如何理解“项目环境”和“依赖安装”的基本思路

---

## 页面功能

这个小项目包含以下功能：

- **标题与文本输出**
  - 使用 `st.title()` 和 `st.write()` 展示页面内容

- **姓名输入框**
  - 使用 `st.text_input()` 获取用户输入

- **年龄滑块**
  - 使用 `st.slider()` 选择数值

- **下拉选择框**
  - 使用 `st.selectbox()` 选择喜欢的工具

- **CSV 文件上传**
  - 使用 `st.file_uploader()` 上传文件
  - 配合 `pandas` 读取并预览表格数据

---

## 技术栈

本项目使用了以下工具：

- **Python**
- **uv**
- **Streamlit**
- **Pandas**

---

## 项目结构

一个典型的项目目录大致如下：

```bash
sample-streamlit-ui/
├── Sample.py
├── README.md
├── pyproject.toml
├── uv.lock
└── .venv/
