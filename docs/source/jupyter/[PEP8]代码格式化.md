
# [PEP8]代码格式化

安装插件，实现`PEP8`风格编程（主要作用于`python`）

## 手动安装

参考：[Prerequisites and Installation Steps](https://jupyterlab-code-formatter.readthedocs.io/en/latest/installation.html)

`conda`安装如下：

```
$ conda install autopep8
$ jupyter labextension install @ryantam626/jupyterlab_code_formatter
$ conda install -c conda-forge jupyterlab_code_formatter
$ jupyter serverextension enable --py jupyterlab_code_formatter
```

安装完成后重启`JupyterLab`

## 配置

参考：[How To Use This Plugin](https://jupyterlab-code-formatter.readthedocs.io/en/latest/how-to-use.html)

配置`Autopep8`，以及设置格式化快捷键

点击菜单栏`Settings -> Advanced Settings Editor`

1. 选择`Jupyterlab Code Formatter`，添加如下配置

```
{  
    "preferences": {
        "default_formatter": {
            "python": "autopep8",
        }
    }
}
```

2. 选择`Keyboard Shortcuts`，添加如下配置

```
{
    "shortcuts": [
        {
            "command": "jupyterlab_code_formatter:autopep8",
            "keys": [
                "Ctrl  L"
            ],
            "selector": ".jp-Notebook.jp-mod-editMode"
        }
    ]
}
```

使用`Ctrl + L`作为格式化代码的快捷键