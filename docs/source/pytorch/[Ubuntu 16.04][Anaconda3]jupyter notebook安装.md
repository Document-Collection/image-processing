
# [Ubuntu 16.04][Anaconda3]jupyter notebook安装

## 安装

先安装`Anaconda`,再安装`jupyter`

    $ conda install jupyter
    # 或
    $ pip install jupyter --user # 出错了

## `not connect to kernel`

参考:[jupyter notebook添加kernel](https://blog.csdn.net/u012151283/article/details/54565467)

我新建了一个`python3.6`环境,在`py36`环境下进行`jupyter`操作,但是一直无法连接到核心

首先查看有效内核

    $ jupyter kernelspec list
    Available kernels:
      python3    /home/zj/.local/share/jupyter/kernels/python3

发现它不在`Anaconda`的安装路径下,进入该目录查看运行操作`kernel.json`

    $ cat kernel.json 
    {
    "argv": [
    "/home/zj/software/anaconda/anaconda3/envs/py36/bin/python",
    "-m",
    "ipykernel_launcher",
    "-f",
    "{connection_file}"
    ],
    "display_name": "Python 3",
    "language": "python"

删除该内核

    $ jupyter kernelspec remove python3

卸载`juyter`并重新安装

    $ pip uninstall jupyter
    $ conda install jupyter


