
# [npm]查询

## 本地已安装依赖

参考：

[hexo 构建静态文件无法生成 index.html 等文件](https://blog.csdn.net/huihut/article/details/73196343)

[node/npm如何查看安装过的模块或包？](https://jingyan.baidu.com/article/9989c746e7f9e9f648ecfe2f.html)

查看当前项目已安装依赖

    $ npm ls --depth 0
    hexo-site@0.0.0 /home/zj/Documents/zjzstu.github.com/blogs
    ├── eslint@5.12.1
    ├── hexo@3.8.0
    ├── hexo-deployer-git@1.0.0
    ├── hexo-generator-archive@0.1.5
    ├── hexo-generator-category@0.1.3
    ├── hexo-generator-index@0.2.1
    ├── hexo-generator-tag@0.2.0
    ├── hexo-renderer-ejs@0.3.1
    ├── hexo-renderer-kramed@0.1.4
    ├── hexo-renderer-stylus@0.3.3
    ├── hexo-server@0.3.3
    └── mkdirp@0.5.1

## 全局已安装依赖

    $ npm ls -g --depth 0
    /home/zj/software/nodejs/node-v10.15.0-linux-x64/lib
    ├── cnpm@6.0.0
    ├── hexo-cli@1.1.0
    └── npm@6.4.1