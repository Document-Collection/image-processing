# image-processing

[![Documentation Status](https://readthedocs.org/projects/zj-image-processing/badge/?version=latest)](https://zj-image-processing.readthedocs.io/zh_CN/latest/?badge=latest) [![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme) [![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org) [![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)

> 图像处理相关的理论算法、实现代码以及使用工具

图像处理是一个综合性研究和开发领域，涉及基础概念、图像算法、代码实现等等。本文档小结相关的内容

* 语言篇
    * [Python](https://zj-image-processing.readthedocs.io/zh_CN/latest/python/%E7%B1%BB%E6%93%8D%E4%BD%9C/)
    * [C++11](https://zj-image-processing.readthedocs.io/zh_CN/latest/cplusplus/%E5%AD%A6%E4%B9%A0C++%E4%B9%8B%E8%B7%AF/)
* 实现篇
    * [OpenCV](https://zj-image-processing.readthedocs.io/zh_CN/latest/opencv/OpenCV%E6%A6%82%E8%BF%B0/)
    * [Matplotlib](https://zj-image-processing.readthedocs.io/zh_CN/latest/matplotlib/%E5%BC%95%E8%A8%80/)
    * [PyTorch](https://zj-image-processing.readthedocs.io/zh_CN/latest/pytorch/%E5%BC%95%E8%A8%80/)
* 算法篇
    * [机器学习](https://zj-image-processing.readthedocs.io/zh_CN/latest/algorithm/machine-learning/)
    * [深度学习](https://zj-image-processing.readthedocs.io/zh_CN/latest/algorithm/deep-learning/)
    * [最优化](https://zj-image-processing.readthedocs.io/zh_CN/latest/algorithm/optimization/)

## 内容列表

- [背景](#背景)
- [安装](#安装)
- [用法](#用法)
- [主要维护人员](#主要维护人员)
- [参与贡献方式](#参与贡献方式)
- [许可证](#许可证)

## 背景

从本科开始就从事图像方向的学习和研究，图像处理是一门理论性强，同时十分重视实践的学科。从图像处理方向入门会接触到许许多多的内容，包括了理论算法、实现代码以及使用的工具，其中有很大一部分值得反复的学习和研究，另外也便于在实际使用过程中，方便环境配置和移植

## 安装

编译文档需要预先安装以下工具：

```
$ pip install mkdocs
```

## 用法

文档有两种使用方式

1. 在线浏览文档：[图像处理](https://zj-image-processing.readthedocs.io/zh_CN/latest/)

2. 本地浏览文档，实现如下：

    ```
    $ git clone https://github.com/zjZSTU/image-processing.git
    $ cd image-processing
    $ mkdocs serve
    ```
    启动本地服务器后即可登录浏览器`localhost:8000`

## 主要维护人员

* zhujian - *Initial work* - [zjZSTU](https://github.com/zjZSTU)

## 参与贡献方式

欢迎任何人的参与！打开[issue](https://github.com/zjZSTU/vscode-guide/issues)或提交合并请求。

注意:

* `GIT`提交，请遵守[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.4/)规范
* 语义版本化，请遵守[Semantic Versioning 2.0.0](https://semver.org)规范
* `README`编写，请遵守[standard-readme](https://github.com/RichardLitt/standard-readme)规范

## 许可证

[Apache License 2.0](LICENSE) © 2019 zjZSTU
