
# RuntimeError: CUDA error: initialization error

参考：[RuntimeError: CUDA error: initialization error](https://blog.csdn.net/yyhaohaoxuexi/article/details/90718501)

>不可在DataLoader或DataSet内将任何数据放到CUDA上，而是等到程序运行出DataLoader之后（也就是到了train里的时候）将数据放到CUDA上。