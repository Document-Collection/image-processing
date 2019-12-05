
# npm和cnpm

参考：

[如何使用NPM？CNPM又是什么？](https://www.jianshu.com/p/f581cf9360a2)

[npm 和 cnpm](https://www.jianshu.com/p/115594f64b41)

[淘宝 NPM 镜像](http://npm.taobao.org/)

## npm vs cnpm

`npm`(`node package management`)是`node.js`的包管理器

`cnpm`是淘宝提供的`npm`镜像

>这是一个完整 npmjs.org 镜像，你可以用此代替官方版本(只读)，同步频率目前为 10分钟 一次以保证尽量与官方服务同步。

## 安装cnpm

安装`cnpm`

    npm install -g cnpm --registry=https://registry.npm.taobao.org

安装完成后使用`cnpm`代替`npm`命令

## 查询

```
$ cnpm -v
cnpm@6.1.0 (/home/zj/software/nodejs/node-v12.13.0-linux-x64/lib/node_modules/cnpm/lib/parse_argv.js)
npm@6.13.0 (/home/zj/software/nodejs/node-v12.13.0-linux-x64/lib/node_modules/cnpm/node_modules/npm/lib/npm.js)
node@12.13.0 (/home/zj/software/nodejs/node-v12.13.0-linux-x64/bin/node)
npminstall@3.23.0 (/home/zj/software/nodejs/node-v12.13.0-linux-x64/lib/node_modules/cnpm/node_modules/npminstall/lib/index.js)
prefix=/home/zj/software/nodejs/node-v12.13.0-linux-x64 
linux x64 4.15.0-64-generic 
registry=https://r.npm.taobao.org
```