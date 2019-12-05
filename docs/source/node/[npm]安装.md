
# [npm]安装

参考：[npm安装卸载命令](https://blog.csdn.net/mezheng/article/details/79650816)

*快捷方式：用`i`替代`install`*

## 本地安装

安装并写入`package.json`的`dependencies`

    npm install xxx –save

安装并写入`package.json`的`devDependencies`

    npm install xxx –save-dev

安装但不写入`package.json`

    npm install xxx

安装`package.json`文件中的依赖到本地`node_modules`文件夹

    npm install

## 全局安装

    npm install -g xxx

## 问题：重新安装一遍后仍然存在`err`

    npm install minipass yallist save-buffer mkdirp wrappy once minimatch inherits string-width ansi-regex number-is-nan strip-ansi is-fullwidth-code-point code-point-at console-control-strings concat-map balanced-match brace-expansion  --save
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.7 (node_modules/fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.7: wanted {"os":"darwin","arch":"any"} (current: {"os":"linux","arch":"x64"})

    + yallist@3.0.3
    + minipass@2.3.5
    + save-buffer@1.1.0
    + inherits@2.0.3
    + ansi-regex@4.0.0
    + wrappy@1.0.2
    + minimatch@3.0.4
    + string-width@3.0.0
    + once@1.4.0
    + code-point-at@1.1.0
    + console-control-strings@1.1.0
    + brace-expansion@1.1.11
    + concat-map@0.0.1
    + balanced-match@1.0.0
    + is-fullwidth-code-point@2.0.0
    + strip-ansi@5.0.0
    + number-is-nan@1.0.1
    + mkdirp@0.5.1
    added 20 packages from 3 contributors, updated 17 packages, moved 3 packages and audited 7176 packages in 6.223s
    found 0 vulnerabilities

    $ npm ls --depth 0
    hexo-site@0.0.0 /home/zj/Documents/zjzstu.github.com/blogs
    ├── ansi-regex@4.0.0
    ├── balanced-match@1.0.0
    ├── brace-expansion@1.1.11
    ├── code-point-at@1.1.0
    ├── concat-map@0.0.1
    ├── console-control-strings@1.1.0
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
    ├── inherits@2.0.3
    ├── is-fullwidth-code-point@2.0.0
    ├── minimatch@3.0.4
    ├── minipass@2.3.5
    ├── mkdirp@0.5.1
    ├── number-is-nan@1.0.1
    ├── once@1.4.0
    ├── save-buffer@1.1.0
    ├── string-width@3.0.0
    ├── strip-ansi@5.0.0
    ├── wrappy@1.0.2
    └── yallist@3.0.3

    npm ERR! missing: mkdirp@0.5.1, required by node-pre-gyp@0.10.3
    npm ERR! missing: minimist@0.0.8, required by mkdirp@0.5.1
    npm ERR! missing: minimatch@3.0.4, required by ignore-walk@3.0.1
    npm ERR! missing: brace-expansion@1.1.11, required by minimatch@3.0.4
    npm ERR! missing: balanced-match@1.0.0, required by brace-expansion@1.1.11
    npm ERR! missing: concat-map@0.0.1, required by brace-expansion@1.1.11
    npm ERR! missing: console-control-strings@1.1.0, required by npmlog@4.1.2
    npm ERR! missing: safe-buffer@5.1.2, required by readable-stream@2.3.6
    npm ERR! missing: safe-buffer@5.1.2, required by string_decoder@1.1.1
    npm ERR! missing: console-control-strings@1.1.0, required by gauge@2.7.4
    npm ERR! missing: strip-ansi@3.0.1, required by gauge@2.7.4
    npm ERR! missing: strip-ansi@3.0.1, required by string-width@1.0.2
    npm ERR! missing: ansi-regex@2.1.1, required by strip-ansi@3.0.1
    npm ERR! missing: minimatch@3.0.4, required by glob@7.1.3
    npm ERR! missing: once@1.4.0, required by glob@7.1.3
    npm ERR! missing: once@1.4.0, required by inflight@1.0.6
    npm ERR! missing: wrappy@1.0.2, required by inflight@1.0.6
    npm ERR! missing: wrappy@1.0.2, required by once@1.4.0
    npm ERR! missing: minipass@2.3.5, required by tar@4.4.8
    npm ERR! missing: mkdirp@0.5.1, required by tar@4.4.8
    npm ERR! missing: safe-buffer@5.1.2, required by tar@4.4.8
    npm ERR! missing: yallist@3.0.3, required by tar@4.4.8
    npm ERR! missing: minipass@2.3.5, required by fs-minipass@1.2.5
    npm ERR! missing: safe-buffer@5.1.2, required by minipass@2.3.5
    npm ERR! missing: yallist@3.0.3, required by minipass@2.3.5
    npm ERR! missing: minipass@2.3.5, required by minizlib@1.2.1

`github`提了一个`bug`：[Ubuntu 16.04 Node.js Hexo npm ERR! missing](https://github.com/nodejs/node/issues/25631)