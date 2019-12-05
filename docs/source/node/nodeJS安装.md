
# nodeJS安装

`hexo`框架基于`Node.JS`实现，经过实践发现同样需要了解一些有关`Node`的知识，记录一下

## 安装

参考[Installation](https://github.com/nodejs/help/wiki/Installation)，使用源码安装`Node.js`

下载已编译安装包[download](https://nodejs.org/en/download/)，当前`LTS`版本为`12.13.0`

    node-v12.13.0-linux-x64.tar.xz

解压文件，参考：[Ubuntu 下解压tar.xz方法](https://www.cnblogs.com/baby123/p/6611169.html)

    # 首先解压xz压缩包
    $ xz -d node-v12.13.0-linux-x64.tar.xz
    # 然后解压tar压缩包
    $ tar xvf node-v12.13.0-linux-x64.tar

设置环境变量，修改`.bashrc`文件

    # Nodejs
    export NODEJS_HOME=/path/to/node-v12.13.0-linux-x64/bin
    export PATH=$NODEJS_HOME:$PATH

刷新文件

    source ~/.bashrc

测试命令

```
$ node -v
v12.13.0

$ npm version
{
  npm: '6.12.0',
  ares: '1.15.0',
  brotli: '1.0.7',
  cldr: '35.1',
  http_parser: '2.8.0',
  icu: '64.2',
  llhttp: '1.1.4',
  modules: '72',
  napi: '5',
  nghttp2: '1.39.2',
  node: '12.13.0',
  openssl: '1.1.1d',
  tz: '2019a',
  unicode: '12.1',
  uv: '1.32.0',
  v8: '7.7.299.13-node.12',
  zlib: '1.2.11'
}

$ npx -v
6.12.0
```

## node更新

参考：[nodejs 如何升级到最新版本](http://www.imooc.com/wenda/detail/550027)

清除缓存

```
npm cache
```

安装n模块

```
npm install -g n
```

升级到最新的稳定版本

```
n stable
```