
# [package.json]脚本运行

参考：[npm run](http://javascript.ruanyifeng.com/nodejs/npm.html#toc12)

`node`支持运行`linux`脚本命令，可以在`package.json`中进行配置

## 配置

在`package.json`文件中预添加脚本，格式如下：

```
{

    "scripts": {
        "script-1": "commands",
        "script-2": "commands",
        "script-3": "commands" 
    }
}
```

配置完成后，使用命令[npm run](https://docs.npmjs.com/cli/run-script.html#description)运行

```
$ npm run script-1
```

## 测试

比如添加测试脚本如下：

```
{
  ...
  ...
  "scripts": {
    "test": "echo \"hello nodejs\""
  },
  ...
  ...
}
```

使用命令`npm run`运行

```
$ npm run test

> nodejs_test@1.0.0 test /home/zj/Downloads/nodejs_test
> echo "hello nodejs"

hello nodejs
```